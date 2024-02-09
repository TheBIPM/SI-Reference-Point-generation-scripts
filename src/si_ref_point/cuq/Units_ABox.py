"""
Units ABox
"""

from rdflib import URIRef, BNode, Graph, Literal
from rdflib import RDF, OWL, SKOS, XSD, RDFS, DCTERMS
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
import si_ref_point.cuq.symbols_format as sf
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os


def nest_mult(expr):
    """Transform
    {'mult': [A, B, C, D...]'}
    into
    {'mult: [A, {'mult': [B, C, D...]}}
    (to be used recusively)
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


def transform_to_graph(expression, PDF, graph):
    """ Tranform any "unit expression" into a graph

    Accepts dicts, strings, lists.

    Returns : rdflib.Graph, rdflib.Bnode

    For representing m/s, for example

    Dicts will be expected to be like
    {"mult": [{"exp": ["metre", 1]}, {"exp": ["second", -1]}]

    Lists will be expected to be like :
    [["metre", 1], ["second", -1]
    (this allows more compact notation in source YAML files

    Strings will be considered to represent a single unit, and turned into an
    URI.


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
        expr_node = PDF.set_unit_uri(expression)

    elif isinstance(expression, dict):
        if "mult" in expression.keys():
            if len(expression["mult"]) == 1:
                # This is not really a product...
                graph, expr_node = transform_to_graph(
                    expression["mult"][0], PDF, graph)
                return graph, expr_node

            # Rearrange products into binary tree (i.e. nested "mult" with
            # only 2 terms, to keep track of order terms)
            expression = nest_mult(expression)

            # set type of expression node
            graph.add((expr_node, RDF.type, PDF.set_uri("UnitProduct")))

            # shortnames
            hasLTerm = PDF.set_uri("hasLeftUnitTerm")
            hasRTerm = PDF.set_uri("hasRightUnitTerm")

            # insert factors
            graph, node = transform_to_graph(expression["mult"][0],
                                             PDF, graph)
            graph.add((expr_node, hasLTerm, node))
            graph, node = transform_to_graph(expression["mult"][1],
                                             PDF, graph)
            graph.add((expr_node, hasRTerm, node))

        elif "exp" in expression.keys():
            if expression["exp"][1] == 1:
                # This is not really a unitPower
                graph, expr_node = transform_to_graph(
                    expression["exp"][0], PDF, graph)
                return graph, expr_node
            else:
                # set type of expression node
                graph.add((expr_node, RDF.type, PDF.set_uri("UnitPower")))

                # shortnames
                hasBase = PDF.set_uri("hasUnitBase")
                hasExponent = PDF.set_uri("hasNumericExponent")

                # insert base and exponent
                graph, node = transform_to_graph(expression["exp"][0],
                                                 PDF, graph)
                exponent = Literal(expression["exp"][1], datatype=XSD.short)
                graph.add((expr_node, hasBase, node))
                graph.add((expr_node, hasExponent, exponent))

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
    PDF = SiElements()
    g = Graph()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(PDF.namespace_units), RDF.type, OWL.Ontology))
    g.add(
        (
            URIRef(PDF.namespace_units),
            SKOS.prefLabel,
            Literal("SI Reference Point - Units and Prefixes", datatype=XSD.string),
        )
    )
    g.add(
        (
            URIRef(PDF.namespace_units),
            RDFS.comment,
            Literal(
                (
                    "Ontology, part of the SI Reference Point, covering "
                    "measurement units (SI base units and SI units with "
                    "special names) and prefixes."
                )
            ),
        )
    )
    g.add(
        (
            URIRef(PDF.namespace_units),
            DCTERMS.created,
            Literal(str(date.today()), datatype=XSD.date),
        )
    )

    # open YAML files with information
    with open(os.path.join(CUQ_FILES_FOLDER, "def_collectors.yaml")) as fp:
        def_collectors = yaml.safe_load(fp)

    # 4) Base unit definitions
    # 4.1) Define the BaseUnit (to which one can subsequently attach several
    # definitions)
    for dc in def_collectors:
        if dc["URI"] is not None:
            element = PDF.set_unit_uri(dc["URI"])

            if dc["URI"] != "gram":
                g.add((element, RDF.type, PDF.SIBaseUnit))
                g.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(fr)"], lang="fr"))
                )
                g.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(en)"], lang="en"))
                )
                g.add(
                    (
                        element,
                        PDF.hasUnitTypeAsString,
                        Literal("SI base unit", lang="en"),
                    )
                )
                g.add(
                    (
                        element,
                        PDF.hasUnitTypeAsString,
                        Literal("Unité SI de base", lang="fr"),
                    )
                )
                g.add(
                    (
                        element,
                        PDF.isUnitOfQtyKind,
                        PDF.set_quantity_uri(dc["isUnitOfQtyKind"]),
                    )
                )
                g.add(
                    (
                        element,
                        PDF.hasSymbol,
                        Literal(dc["hasSymbol"], datatype=XSD.string),
                    )
                )
                if "hasPrefix" in dc.keys():
                    g.add((element, RDF.type, PDF.set_uri("PrefixedUnit")))
                    g.add(
                        (
                            element,
                            PDF.set_uri("hasPrefix"),
                            PDF.set_prefix_uri(dc["hasPrefix"]),
                        )
                    )
                if "hasNonPrefixedUnit" in dc.keys():
                    g.add(
                        (
                            element,
                            PDF.set_uri("hasNonPrefixedUnit"),
                            PDF.set_unit_uri(dc["hasNonPrefixedUnit"]),
                        )
                    )

                for i, dfn in enumerate(dc["definitions"]):
                    curr_def = dfn
                    try:
                        next_def = dc["definitions"][i + 1]
                    except IndexError:
                        next_def = None
                    if curr_def is not None:
                        g.add((element, PDF.hasDefinition, PDF.set_uri(curr_def)))
                        if next_def is not None:
                            g.add(
                                (
                                    PDF.set_uri(curr_def),
                                    PDF.hasNextDefinition,
                                    PDF.set_uri(next_def),
                                )
                            )

                    if i > 0:
                        prev_def = dc["definitions"][i - 1]
                    else:
                        prev_def = None
                    if curr_def is not None:
                        if prev_def is not None:
                            g.add(
                                (
                                    PDF.set_uri(curr_def),
                                    PDF.hasPreviousDefinition,
                                    PDF.set_uri(prev_def),
                                )
                            )
            else:  # gram
                g.add((element, RDF.type, PDF.MeasurementUnit))
                g.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(fr)"], lang="fr"))
                )
                g.add(
                    (element, SKOS.prefLabel, Literal(dc["prefLabel(en)"], lang="en"))
                )
                g.add(
                    (
                        element,
                        PDF.isUnitOfQtyKind,
                        PDF.set_quantity_uri(dc["isUnitOfQtyKind"]),
                    )
                )
                g.add(
                    (
                        element,
                        PDF.hasSymbol,
                        Literal(dc["hasSymbol"], datatype=XSD.string),
                    )
                )

    # 4.2 Declare all definitions
    # uri_text values are a concatenation of the lowercase unit name and the
    # year of the definition, e.g., ampere2018

    with open(
        os.path.join(CUQ_FILES_FOLDER, "base_units_defs.yaml"), encoding="utf8"
    ) as fp:
        basedefs = yaml.safe_load(fp)
    with open(os.path.join(CUQ_FILES_FOLDER, "notes.yaml"), encoding="utf8") as fp:
        notes = yaml.safe_load(fp)

    for bdef in basedefs:
        # add data
        if bdef["URI"] is not None:
            element = PDF.set_uri(bdef["URI"])
            g.add((element, RDF.type, PDF.Definition))
            g.add((element, SKOS.prefLabel, Literal(bdef["prefLabel_fr"], lang="fr")))
            g.add((element, SKOS.prefLabel, Literal(bdef["prefLabel_en"], lang="en")))
            g.add(
                (
                    element,
                    PDF.hasStartValidity,
                    Literal(bdef["hasStartValidity"], datatype=XSD.date),
                )
            )
            if bdef["hasEndValidity"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasEndValidity,
                        Literal(bdef["hasEndValidity"], datatype=XSD.date),
                    )
                )
            if bdef["hasDefiningText_fr"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasDefiningText,
                        Literal(
                            sf.formattxt(bdef["hasDefiningText_fr"],
                                         "latex",
                                         add_delim=True), lang="fr"
                        ),
                    )
                )
            if bdef["hasDefiningText_en"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasDefiningText,
                        Literal(
                            sf.formattxt(bdef["hasDefiningText_en"],
                                         "latex",
                                         add_delim=True), lang="en"
                        ),
                    )
                )
            g.add((element,
                   PDF.hasDefiningResolution,
                   PDF.set_resolution_uri(bdef["hasDefiningResolution"])))

            if bdef["hasDefiningEquation"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasDefiningEquation,
                        Literal(
                            sf.formattxt(
                                bdef["hasDefiningEquation"], "latex", add_delim=False
                            ),
                            datatype=XSD.string,
                        ),
                    )
                )
            if bdef["hasDefiningConstant"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasDefiningConstant,
                        PDF.set_constant_uri(bdef["hasDefiningConstant"]),
                    )
                )
            if bdef["Status"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasStatus,
                        Literal(bdef["Status"], datatype=XSD.string),
                    )
                )
            # Only used for kilogram in base defs
            if "PrefixRestriction" not in bdef:
                bdef['PrefixRestriction'] = False
            g.add(
                (
                    element,
                    PDF.prefixRestriction,
                    Literal(bdef['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
            )

            # notes
            # get all the notes for a definition
            for note in notes:
                if note["uri"] == bdef["URI"]:
                    notenode = PDF.set_uri(
                        "{}note{}".format(bdef["URI"], note["index"])
                    )
                    g.add((element, PDF.hasDefinitionNote, notenode))
                    g.add((notenode, RDF.type, PDF.DefinitionNote))
                    g.add((notenode, PDF.hasNoteIndex, Literal(note["index"])))
                    g.add(
                        (
                            notenode,
                            PDF.hasNoteText,
                            Literal(sf.formattxt(note["note_en"], "latex",
                                                 add_delim=True), lang="en"),
                        )
                    )
                    g.add(
                        (
                            notenode,
                            PDF.hasNoteText,
                            Literal(sf.formattxt(note["note_fr"], "latex",
                                                 add_delim=True), lang="fr"),
                        )
                    )

    # 5 SI Units Special Names
    with open(os.path.join(CUQ_FILES_FOLDER, "si_units_special_names.yaml")) as fp:
        si_spec_list = yaml.safe_load(fp)

    for sisp in si_spec_list:
        if sisp["URI"] is not None:
            element = PDF.set_unit_uri(sisp["URI"])
            g.add((element, RDF.type, PDF.SISpecialNamedUnit))
            g.add(
                (
                    element,
                    PDF.hasUnitTypeAsString,
                    Literal("Named SI derived unit", lang="en"),
                )
            )
            g.add(
                (
                    element,
                    PDF.hasUnitTypeAsString,
                    Literal("Unité SI dérivée ayant un nom spécial", lang="fr"),
                )
            )
            g.add((element, SKOS.prefLabel, Literal(sisp["prefLabel_fr"], lang="fr")))
            g.add((element, SKOS.prefLabel, Literal(sisp["prefLabel_en"], lang="en")))
            g.add(
                (
                    element,
                    PDF.hasSymbol,
                    Literal(sisp["Symbol"], datatype=XSD.string),
                )
            )
            g.add(
                (
                    element,
                    PDF.isUnitOfQtyKind,
                    PDF.set_quantity_uri(sisp["UnitOfQtyKind"]),
                )
            )
            g.add(
                (
                    element,
                    PDF.hasDefiningResolution,
                    URIRef(PDF.set_cgpm_uri(sisp["hasDefiningResolution"])),
                )
            )

            if "inOtherSIUnits" in sisp and sisp["inOtherSIUnits"]:
                g, node = transform_to_graph(sisp["inOtherSIUnits"],
                                             PDF, g)
                g.add((element, PDF.inOtherSIUnits, node))

            if "inBaseSIUnits" in sisp and sisp["inBaseSIUnits"]:
                g, node = transform_to_graph(sisp["inBaseSIUnits"],
                                             PDF, g)
                g.add((element, PDF.inBaseSIUnits, node))

            if sisp["hasDefiningEquation"]:
                g.add(
                    (
                        element,
                        PDF.hasDefiningEquation,
                        Literal(
                            sf.formattxt(
                                sisp["hasDefiningEquation"], "latex", add_delim=False
                            ),
                            datatype=XSD.string,
                        ),
                    )
                )
            # Only used for degreeCelsius in sisp
            if "PrefixRestriction" not in sisp:
                sisp['PrefixRestriction'] = False
            g.add(
                (
                    element,
                    PDF.prefixRestriction,
                    Literal(sisp['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
            )


    # 6) non SI units
    with open(os.path.join(CUQ_FILES_FOLDER, "non_si_units.yaml")) as fp:
        non_si_list = yaml.safe_load(fp)

    for nsi in non_si_list:
        if nsi["URI"] is not None:
            element = PDF.set_unit_uri(nsi["URI"])
            g.add((element, RDF.type, PDF.nonSIUnit))
            g.add(
                (
                    element,
                    PDF.hasUnitTypeAsString,
                    Literal("Non-SI unit accepted for use with the SI", lang="en"),
                )
            )
            g.add(
                (
                    element,
                    PDF.hasUnitTypeAsString,
                    Literal(
                        "Unité en dehors du SI " "dont l'usage est accepté avec le SI",
                        lang="fr",
                    ),
                )
            )
            g.add((element, SKOS.prefLabel, Literal(nsi["prefLabel_fr"], lang="fr")))
            g.add((element, SKOS.prefLabel, Literal(nsi["prefLabel_en"], lang="en")))
            g.add(
                (
                    element,
                    PDF.hasSymbol,
                    Literal(nsi["Symbol"], datatype=XSD.string),
                )
            )
            if "AltSymbol" in nsi:
                g.add(
                    (
                        element,
                        PDF.hasAltSymbol,
                        Literal(nsi["AltSymbol"], datatype=XSD.string),
                    )
                )

            if "PrefixRestriction" not in nsi:
                nsi['PrefixRestriction'] = False
            g.add(
                (
                    element,
                    PDF.prefixRestriction,
                    Literal(nsi['PrefixRestriction'],
                            datatype=XSD.boolean),
                )
                )

            g.add(
                (
                    element,
                    PDF.isUnitOfQtyKind,
                    PDF.set_quantity_uri(nsi["UnitOfQtyKind"]),
                )
            )
            if "ConversionFactor" in nsi:
                unit_multiple = BNode()
                hasUnitTerm = PDF.set_uri("hasUnitTerm")
                hasNumericFactor = PDF.set_uri("hasNumericFactor")
                conversion_factor = Literal(nsi["ConversionFactor"])
                g, conversion_unit = transform_to_graph(nsi["ConversionUnit"],
                                                        PDF, g)
                g.add((unit_multiple, RDF.type, PDF.set_uri("UnitMultiple")))
                g.add((unit_multiple, hasUnitTerm, conversion_unit))
                g.add((unit_multiple, hasNumericFactor, conversion_factor))
                g.add((element, PDF.inOtherSIUnits, unit_multiple))

    return g


if __name__ == "__main__":
    main()
