"""
Units ABox
"""

from datetime import datetime, timezone
import git
import os
import logging
import yaml
from decimal import Decimal
from rdflib import Graph, URIRef, BNode, Literal, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, PROV
from si_ref_point.tboxes.si_tbox import SiElements
import si_ref_point.aboxes.symbols_format as sf
from si_ref_point.settings import PKG_ROOT, CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, SI_FILES_FOLDER, \
    GITHUB_BASE_PATH, SIDFWBASE, SIRPVERSION


def nest_mult(expr):
    """Transform
    {'mult': [A, B, C, D...]'}
    into
    {'mult: [A, {'mult': [B, C, D...]}}
    (to be used recursively)
    """
    # Check number of terms
    if len(expr['mult']) == 1:
        return expr
    left_term = expr['mult'][0]
    right_term = expr['mult'][1:]
    if len(right_term) == 1:
        return {'mult': [left_term, right_term[0]]}
    else:
        return {'mult': [left_term,
                         nest_mult({'mult': right_term})]}


def transform_to_graph(expression, si_graph, graph):
    """ Transform any "unit expression" into a graph

    Accepts dicts, strings, lists.

    Returns : rdflib.Graph, rdflib.Bnode

    For representing m/s, for example

    Dicts will be expected to be like
    {"mult": [{"exp": ["metre", 1]}, {"exp": ["second", -1]}]}

    Lists will be expected to be like :
    [["metre", 1], ["second", -1]
    (this allows more compact notation in source YAML files)

    Strings will be considered to represent a single unit, and turned into a URI.


    This function calls itself in order to walk the tree of nested UnitProduct
    and UnitPower objects.
    """

    if isinstance(expression, list):
        # turn into a dict
        tmp_expr = {"mult": []}
        for item in expression:
            tmp_expr['mult'].append({"exp": [item[0], item[1]]})
        expression = tmp_expr
    expr_node = BNode()

    if isinstance(expression, str):
        expr_node = si_graph.set_unit_uri(expression)

    elif isinstance(expression, dict):
        if "mult" in expression.keys():
            if len(expression["mult"]) == 1:
                # This is not really a product...
                graph, expr_node = transform_to_graph(
                    expression["mult"][0], si_graph, graph)
                return graph, expr_node

            # Rearrange products into binary tree (i.e. nested "mult" with
            # only 2 terms, to keep track of order terms)
            expression = nest_mult(expression)

            # set type of expression node
            graph.add((expr_node, RDF.type, si_graph.set_uri("UnitProduct")))

            # shortnames
            has_l_term = si_graph.set_uri("hasLeftUnitTerm")
            has_r_term = si_graph.set_uri("hasRightUnitTerm")

            # insert factors
            graph, node = transform_to_graph(expression["mult"][0],
                                             si_graph, graph)
            graph.add((expr_node, has_l_term, node))
            graph, node = transform_to_graph(expression["mult"][1],
                                             si_graph, graph)
            graph.add((expr_node, has_r_term, node))

        elif "exp" in expression.keys():
            if expression["exp"][1] in [1, "1"]:
                # This is not really a unitPower
                graph, expr_node = transform_to_graph(
                    expression["exp"][0], si_graph, graph)
                return graph, expr_node
            else:
                # set type of expression node
                graph.add((expr_node, RDF.type, si_graph.set_uri("UnitPower")))

                # shortnames
                has_base = si_graph.set_uri("hasUnitBase")
                has_exponent = si_graph.set_uri("hasNumericExponent")

                # insert base and exponent
                graph, node = transform_to_graph(expression["exp"][0],
                                                 si_graph, graph)
                exponent = Literal(expression["exp"][1], datatype=XSD.short)
                graph.add((expr_node, has_base, node))
                graph.add((expr_node, has_exponent, exponent))

        else:
            raise ValueError(
                f"Unrecognized keys in expression-object: {expression.keys()}."
            )

    else:
        raise ValueError(
            f"Expecting either a string, a list or dict. Got '{type(expression)}'."
        )

    return graph, expr_node


def main():
    """main of Units A-box"""
    # get the predicates and classes that are common to all cuq files
    si_graph = SiElements()
    # produce a separate graph for the units
    units_graph = Graph()


    # 1) Define the namespaces within (base)/SI
    #   (for the moment, these bindings are made 'manually'.
    #    They should be proposed as a common function [e.g. in si_tbox.py])
    units_graph.bind("constants",si_graph.namespace_constants)
    units_graph.bind("quantities",si_graph.namespace_quantities)
    units_graph.bind("units",si_graph.namespace_units)
    units_graph.bind("si",si_graph.namespace)

    # 2) Add annotations to the units-graph

    # 2.1 General annotations (type, labels, comments etc)
    units_graph.add(
        (
            URIRef(si_graph.namespace_units),
            RDF.type,
            OWL.Ontology)
    )
    units_graph.add(
        (
            URIRef(si_graph.namespace_units),
            SKOS.prefLabel,
            Literal("SI Reference Point - Units and Prefixes", datatype=XSD.string),
        )
    )

    units_graph.add(
        (URIRef(si_graph.namespace_units),
            RDFS.comment,
            Literal(
                ("Ontology, part of the SI Reference Point, covering "
                    "measurement units (SI base units and SI units with "
                    "special names) and prefixes."),
                datatype=XSD.string))
    )

    # SemVer
    version_iri = URIRef(SIDFWBASE + "/" + SIRPVERSION + "/units/")
    units_graph.add((URIRef(si_graph.namespace_units), OWL.versionIRI, version_iri))
    units_graph.add((URIRef(si_graph.namespace_units), OWL.versionInfo, Literal(SIRPVERSION, datatype=XSD.string)))

    # 2.2 Versioning (using PROVENANCE vocabulary)
    timestamp = datetime.now(timezone.utc)                              # get the system time (in UTC)
    uri_timestamp = timestamp.strftime("%Y%m%d%H%M%SZ")                 # used to identify uniquely the produced TTL file (entity)
    startedAt_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")      # used with the predicate 'startedAtTime' of the corresponding activity
    repo = git.Repo(PKG_ROOT, search_parent_directories=True)
    sha = repo.head.object.hexsha
    #     2.2.1 Agent
    #     declare this code as an 'agent' (in the sense of PROVENANCE)
    #     and define URI to a specific version by using its commit on GitHub
    agents = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/si_tbox.py",
              GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/units_abox.py"]
    for agent_sw in agents:
        units_graph.add(
            (URIRef(agent_sw),
                RDF.type,
                PROV.Agent)
        )

    #     2.2.2 Entity
    #     declare the sources (YAML files) as 'entity' (in the sense of PROVENANCE)
    #     The manually produced YAML files are stored on GITHUB. Their hexsha together
    #     with the path are used as a unique identifier
    source_list = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/def_collectors.yaml",
                   GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/base_units_defs.yaml",
                   GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/notes.yaml",
                   GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/si_units_special_names.yaml",
                   GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/non_si_units.yaml"]

    for source in source_list:
        units_graph.add(
            (URIRef(source),
                RDF.type,
                PROV.Entity)
        )

    #     declare the ttl output as an 'entity' (in the sense of PROVENANCE)
    #     make the entity unique by adding the timestamp to the identifier of the output file
    units_out_entity = "units_"+uri_timestamp+".ttl"
    units_graph.add(
        (si_graph.set_entity_uri(units_out_entity),
            RDF.type,
            PROV.Entity)
    )

    #     2.2.3 Activity
    #     declare the units_ttl_generation as 'activity' (in the sense of PROVENANCE)
    #     make the activity unique by adding the timestamp to the identifier of the activity
    activity = 'units_'+uri_timestamp + '.ttl_generation'
    units_graph.add(
        (si_graph.set_activity_uri(activity),
        RDF.type,
        PROV.Activity)
        )

    #     2.2.4 Link activity, agent, entities
    #     activity - agent
    for agent_sw in agents:
        units_graph.add(
            (si_graph.set_activity_uri(activity),
            PROV.wasAssociatedWith,
            URIRef(agent_sw))
        )
    units_graph.add(
        (si_graph.set_activity_uri(activity),
            PROV.startedAtTime,
            Literal(startedAt_timestamp, datatype=XSD.dateTime))
    )
    #   output entity - source entities
    for source in source_list:
        units_graph.add(
            (si_graph.set_entity_uri(units_out_entity),
             PROV.wasDerivedFrom,
             URIRef(source))
        )

    #    output entity - agent
    for agent_sw in agents:
        units_graph.add(
            (si_graph.set_entity_uri(units_out_entity),
                PROV.wasAttributedTo,
                URIRef(agent_sw))
        )
    #    output entity - activity
    units_graph.add(
        (si_graph.set_entity_uri(units_out_entity),
            PROV.wasGeneratedBy,
            si_graph.set_activity_uri(activity))
    )

    # 2.3 Licence
    units_graph.add(
         (URIRef(si_graph.namespace_units),
          DCTERMS.license,
          URIRef(CC_LICENCE))
    )
    units_graph.add(
        (URIRef(si_graph.namespace_units),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_EN,lang="en"))
    )
    units_graph.add(
        (URIRef(si_graph.namespace_units),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_FR,lang="fr"))
    )

    # 3) Build units graph

    # 3.1 open YAML file def_collector
    with open(os.path.join(SI_FILES_FOLDER, "def_collectors.yaml"), encoding='utf-8') as fp:
        def_collectors = yaml.safe_load(fp)

    # 3.2 Base unit definitions
    # Define the BaseUnit (to which one can subsequently attach several
    # definitions)
    for dc in def_collectors["data"]:
        if dc["URI"] is not None:
            element = si_graph.set_unit_uri(dc["URI"])

            if dc["URI"] not in ["gram", "one"]:
                units_graph.add((element, RDF.type, si_graph.si_base_unit))
                units_graph.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(fr)"], lang="fr"))
                )
                units_graph.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(en)"], lang="en"))
                )
                units_graph.add(
                    (
                        element,
                        si_graph.has_unit_type_as_string,
                        Literal("SI base unit", lang="en"),
                    )
                )
                units_graph.add(
                    (
                        element,
                        si_graph.has_unit_type_as_string,
                        Literal("Unité SI de base", lang="fr"),
                    )
                )
                # UnitOfQtyKind can be list or single item
                if isinstance(dc["isUnitOfQtyKind"], list):
                    qty_kind_list = dc["isUnitOfQtyKind"]
                else:
                    qty_kind_list = [dc["isUnitOfQtyKind"]]

                for qty_kind in qty_kind_list:
                    units_graph.add(
                        (
                            element,
                            si_graph.is_unit_of_qty_kind,
                            si_graph.set_quantity_uri(qty_kind),
                        )
                    )
                units_graph.add(
                    (
                        element,
                        si_graph.has_symbol,
                        Literal(dc["hasSymbol"], datatype=XSD.string),
                    )
                )
                if "hasPrefix" in dc.keys():
                    units_graph.add((element, RDF.type, si_graph.set_uri("PrefixedUnit")))
                    units_graph.add(
                        (
                            element,
                            si_graph.set_uri("hasPrefix"),
                            si_graph.set_prefix_uri(dc["hasPrefix"]),
                        )
                    )
                if "hasNonPrefixedUnit" in dc.keys():
                    units_graph.add(
                        (
                            element,
                            si_graph.set_uri("hasNonPrefixedUnit"),
                            si_graph.set_unit_uri(dc["hasNonPrefixedUnit"]),
                        )
                    )

                for i, dfn in enumerate(dc["definitions"]):
                    curr_def = dfn
                    try:
                        next_def = dc["definitions"][i + 1]
                    except IndexError:
                        next_def = None
                    if curr_def is not None:
                        units_graph.add(
                                (
                                    element,
                                    si_graph.has_definition,
                                    si_graph.set_uri(curr_def)
                                )
                            )
                        if next_def is not None:
                            units_graph.add(
                                (
                                    si_graph.set_uri(curr_def),
                                    si_graph.has_next_definition,
                                    si_graph.set_uri(next_def),
                                )
                            )

                    if i > 0:
                        prev_def = dc["definitions"][i - 1]
                    else:
                        prev_def = None
                    if curr_def is not None:
                        if prev_def is not None:
                            units_graph.add(
                                (
                                    si_graph.set_uri(curr_def),
                                    si_graph.has_previous_definition,
                                    si_graph.set_uri(prev_def),
                                )
                            )
            else:  # gram, one
                units_graph.add((element, RDF.type, si_graph.measurement_unit))
                units_graph.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(fr)"], lang="fr"))
                )
                units_graph.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(en)"], lang="en"))
                )
                if "prefixRestriction" in dc:
                    units_graph.add(
                        (element,
                         si_graph.prefix_restriction,
                         Literal(dc["prefixRestriction"], datatype=XSD.boolean),
                        )
                    )
                if "isUnitOfQtyKind" in dc:  # "one" has many unlisted quantity kinds
                    units_graph.add(
                        (
                            element,
                            si_graph.is_unit_of_qty_kind,
                            si_graph.set_quantity_uri(dc["isUnitOfQtyKind"]),
                        )
                    )
                units_graph.add(
                    (
                        element,
                        si_graph.has_symbol,
                        Literal(dc["hasSymbol"], datatype=XSD.string),
                    )
                )

    # 3.3 Declare all definitions
    # uri_text values are a concatenation of the lowercase unit name and the
    # year of the definition, e.g., ampere2018

    with open(
        os.path.join(SI_FILES_FOLDER, "base_units_defs.yaml"), encoding="utf8"
    ) as fp:
        basedefs = yaml.safe_load(fp)
    with open(os.path.join(SI_FILES_FOLDER, "notes.yaml"), encoding="utf8") as fp:
        notes = yaml.safe_load(fp)


    for bdef in basedefs["data"]:
        # add data
        if bdef["URI"] is not None:
            element = si_graph.set_uri(bdef["URI"])
            units_graph.add((element, RDF.type, si_graph.definition))
            units_graph.add((element, SKOS.prefLabel, Literal(bdef["prefLabel_fr"], lang="fr")))
            units_graph.add((element, SKOS.prefLabel, Literal(bdef["prefLabel_en"], lang="en")))
            units_graph.add(
                (
                    element,
                    si_graph.has_start_validity,
                    Literal(bdef["hasStartValidity"], datatype=XSD.date),
                )
            )
            if bdef["hasEndValidity"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_end_validity,
                        Literal(bdef["hasEndValidity"], datatype=XSD.date),
                    )
                )
            if bdef["hasDefiningText_fr"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_defining_text,
                        Literal(
                            sf.formattxt(bdef["hasDefiningText_fr"],
                                         "latex",
                                         add_delim=True), lang="fr"
                        ),
                    )
                )
            if bdef["hasDefiningText_en"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_defining_text,
                        Literal(
                            sf.formattxt(bdef["hasDefiningText_en"],
                                         "latex",
                                         add_delim=True), lang="en"
                        ),
                    )
                )
            units_graph.add((element,
                   si_graph.has_defining_resolution,
                   si_graph.set_resolution_uri(bdef["hasDefiningResolution"])))

            if bdef["hasDefiningEquation"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_defining_equation,
                        Literal(
                            sf.formattxt(
                                bdef["hasDefiningEquation"], "latex", add_delim=False
                            ),
                            datatype=XSD.string,
                        ),
                    )
                )
            if bdef["hasDefiningConstant"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_defining_constant,
                        si_graph.set_constant_uri(bdef["hasDefiningConstant"]),
                    )
                )
            if bdef["Status"] is not None:
                units_graph.add(
                    (
                        element,
                        si_graph.has_status,
                        Literal(bdef["Status"], datatype=XSD.string),
                    )
                )
            # Only used for kilogram in base defs
            if "PrefixRestriction" not in bdef:
                bdef['PrefixRestriction'] = False
            units_graph.add(
                (
                    element,
                    si_graph.prefix_restriction,
                    Literal(bdef['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
            )

            # notes
            # get all the notes for a definition
            for note in notes["data"]:
                if note["uri"] == bdef["URI"]:
                    # notenode = si_graph.set_uri(
                    #     "{}note{}".format(bdef["URI"], note["index"])
                    # )
                    notenode = si_graph.set_uri(
                        f"""{bdef['URI']}note{note['index']}"""
                        )

                    units_graph.add((element, si_graph.has_definition_note, notenode))
                    units_graph.add((notenode, RDF.type, si_graph.definition_note))
                    units_graph.add((notenode, si_graph.has_note_index, Literal(note["index"])))
                    units_graph.add(
                        (
                            notenode,
                            si_graph.has_note_text,
                            Literal(sf.formattxt(note["note_en"], "latex",
                                                 add_delim=True), lang="en"),
                        )
                    )
                    units_graph.add(
                        (
                            notenode,
                            si_graph.has_note_text,
                            Literal(sf.formattxt(note["note_fr"], "latex",
                                                 add_delim=True), lang="fr"),
                        )
                    )

    # 3.4 SI Units Special Names
    with open(os.path.join(SI_FILES_FOLDER, "si_units_special_names.yaml"),encoding='utf-8') as fp:
        si_spec_list = yaml.safe_load(fp)

    for sisp in si_spec_list["data"]:
        if sisp["URI"] is not None:
            element = si_graph.set_unit_uri(sisp["URI"])
            units_graph.add((element, RDF.type, si_graph.si_special_named_unit))
            units_graph.add(
                (
                    element,
                    si_graph.has_unit_type_as_string,
                    Literal("Named SI derived unit", lang="en"),
                )
            )
            units_graph.add(
                (
                    element,
                    si_graph.has_unit_type_as_string,
                    Literal("Unité SI dérivée ayant un nom spécial", lang="fr"),
                )
            )
            units_graph.add((element, SKOS.prefLabel, Literal(sisp["prefLabel_fr"], lang="fr")))
            units_graph.add((element, SKOS.prefLabel, Literal(sisp["prefLabel_en"], lang="en")))
            units_graph.add(
                (
                    element,
                    si_graph.has_symbol,
                    Literal(sisp["Symbol"], datatype=XSD.string),
                )
            )
            # UnitOfQtyKind can be list or single item
            if isinstance(sisp["UnitOfQtyKind"], list):
                qty_kind_list = sisp["UnitOfQtyKind"]
            else:
                qty_kind_list = [sisp["UnitOfQtyKind"]]

            for qty_kind in qty_kind_list:
                units_graph.add(
                    (
                        element,
                        si_graph.is_unit_of_qty_kind,
                        si_graph.set_quantity_uri(qty_kind),
                    )
                )
            units_graph.add(
                (
                    element,
                    si_graph.has_defining_resolution,
                    URIRef(si_graph.set_cgpm_uri(sisp["hasDefiningResolution"])),
                )
            )

            if "inOtherSIUnits" in sisp and sisp["inOtherSIUnits"]:
                units_graph, node = transform_to_graph(sisp["inOtherSIUnits"],
                                             si_graph, units_graph)
                units_graph.add((element, si_graph.in_other_si_units, node))


            if "inBaseSIUnits" in sisp and sisp["inBaseSIUnits"]:
                units_graph, node = transform_to_graph(sisp["inBaseSIUnits"],
                                             si_graph, units_graph)
                units_graph.add((element, si_graph.in_base_si_units, node))

            # Only used for degreeCelsius in sisp
            if "PrefixRestriction" not in sisp:
                sisp['PrefixRestriction'] = False
            units_graph.add(
                (
                    element,
                    si_graph.prefix_restriction,
                    Literal(sisp['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
            )


    # 3.5 non SI units
    with open(os.path.join(SI_FILES_FOLDER, "non_si_units.yaml"),encoding='utf-8') as fp:
        non_si_list = yaml.safe_load(fp)

    for nsi in non_si_list["data"]:
        if nsi["URI"] is not None:
            element = si_graph.set_unit_uri(nsi["URI"])
            units_graph.add((element, RDF.type, si_graph.non_si_unit))
            units_graph.add(
                (
                    element,
                    si_graph.has_unit_type_as_string,
                    Literal("Non-SI unit", lang="en"),
                )
            )
            units_graph.add(
                (
                    element,
                    si_graph.has_unit_type_as_string,
                    Literal(
                        "Unité en dehors du SI",
                        lang="fr",
                    ),
                )
            )
            units_graph.add((element, SKOS.prefLabel, Literal(nsi["prefLabel_fr"], lang="fr")))
            units_graph.add((element, SKOS.prefLabel, Literal(nsi["prefLabel_en"], lang="en")))
            units_graph.add(
                (
                    element,
                    si_graph.has_symbol,
                    Literal(nsi["Symbol"], datatype=XSD.string),
                )
            )
            if "AltSymbol" in nsi:
                units_graph.add(
                    (
                        element,
                        si_graph.has_alt_symbol,
                        Literal(nsi["AltSymbol"], datatype=XSD.string),
                    )
                )

            if "hasPrefix" in nsi:
                units_graph.add((element, RDF.type, si_graph.set_uri("PrefixedUnit")))
                units_graph.add(
                    (
                        element,
                        si_graph.set_uri("hasPrefix"),
                        si_graph.set_prefix_uri(nsi["hasPrefix"]),
                    )
                )

            if "hasNonPrefixedUnit" in nsi:
                units_graph.add(
                    (
                        element,
                        si_graph.set_uri("hasNonPrefixedUnit"),
                        si_graph.set_unit_uri(nsi["hasNonPrefixedUnit"]),
                    )
                )

            if "PrefixRestriction" not in nsi:
                nsi['PrefixRestriction'] = False
            units_graph.add(
                (
                    element,
                    si_graph.prefix_restriction,
                    Literal(nsi['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
                )

            # UnitOfQtyKind can be list or single item
            if isinstance(nsi["UnitOfQtyKind"], list):
                qty_kind_list = nsi["UnitOfQtyKind"]
            else:
                qty_kind_list = [nsi["UnitOfQtyKind"]]

            for qty_kind in qty_kind_list:
                units_graph.add(
                    (
                        element,
                        si_graph.is_unit_of_qty_kind,
                        si_graph.set_quantity_uri(qty_kind),
                    )
                )
            if "ConversionFactor" in nsi:
                unit_multiple = BNode()
                has_unit_term = si_graph.set_uri("hasUnitTerm")
                has_numeric_factor = si_graph.set_uri("hasNumericFactor")
                has_numeric_factor_as_string = si_graph.set_uri("hasNumericFactorAsString")

                if isinstance(nsi["ConversionFactor"], int):
                    conv_factor_type = XSD.integer
                elif isinstance(nsi["ConversionFactor"], str):
                    conv_factor_type = XSD.decimal
                else:
                    logging.error('Error : unknown ConversionFactor type : %s ',
                                  nsi["ConversionFactor"])
                    conv_factor_type = None
                conversion_factor = Literal(str(format(Decimal(nsi["ConversionFactor"]), 'f')),
                                           datatype=conv_factor_type)
                conversion_factor_as_string = Literal(
                    nsi["ConversionFactorAsString"],
                    datatype=XSD.string)
                units_graph, conversion_unit = transform_to_graph(nsi["ConversionUnit"],
                                                        si_graph, units_graph)
                units_graph.add((unit_multiple, RDF.type, si_graph.set_uri("UnitMultiple")))
                units_graph.add((unit_multiple, has_unit_term, conversion_unit))
                units_graph.add((unit_multiple, has_numeric_factor, conversion_factor))
                units_graph.add((unit_multiple, has_numeric_factor_as_string,
                       conversion_factor_as_string))
                units_graph.add((element, si_graph.in_other_si_units, unit_multiple))

    return units_graph


if __name__ == "__main__":
    main()
