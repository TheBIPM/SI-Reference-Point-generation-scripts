"""
Units ABox
"""

from rdflib import URIRef, BNode, Graph, Literal
from rdflib import RDF, OWL, SKOS, XSD, RDFS, DCTERMS
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os
import re
import si_ref_point.cuq.symbols_format as sf


def parse_fragments(fragments, syntax):
    expression = {"mult": []}

    for i, frag in enumerate(fragments):
        not_last_fragment = i < len(fragments) - 1

        if re.fullmatch(syntax["variable"], frag):
            # get variable name
            var_name = re.findall(syntax["var_name"], frag)[0]

            if not_last_fragment:
                # check if next fragment indicates exponentiation
                if re.fullmatch(syntax["exponent"], fragments[i + 1]):
                    exp_number = re.findall(syntax["exp_number"], fragments[i + 1])[0]
                    expression["mult"].append({"exp": [var_name, exp_number]})
                else:
                    expression["mult"].append(var_name)
            else:
                expression["mult"].append(var_name)

        if re.fullmatch(syntax["division"], frag):
            if not_last_fragment:
                # represent division as exponentiation
                div_expr = parse_fragments(fragments[i + 1 :], syntax)
                expression["mult"].append({"exp": [div_expr, "-1"]})
                break

    # reduce expression, if only one factor
    if len(expression["mult"]) == 1:
        expression = expression["mult"][0]

    return expression


def transform_to_graph(expression, PDF, graph, symbols):
    expr_node = BNode()

    if isinstance(expression, str):
        # default
        expr_node = Literal(expression)

        # check if lookup possible
        if expression in symbols.keys():
            if "uri" in symbols[expression]:
                unit_short_uri = symbols[expression]["uri"]
                unit_name = unit_short_uri.split(":")[1]
                expr_node = PDF.set_unit_uri(unit_name)

    elif isinstance(expression, dict):
        if "mult" in expression.keys():
            # set type of expression node
            graph.add((expr_node, RDF.type, PDF.set_operation_uri("Multiplication")))

            # shortnames
            hasFactor = PDF.set_uri("hasFactor")

            # insert factors
            for factor in expression["mult"]:
                graph, node = transform_to_graph(factor, PDF, graph, symbols)
                graph.add((expr_node, hasFactor, node))

        elif "exp" in expression.keys():
            # set type of expression node
            graph.add((expr_node, RDF.type, PDF.set_operation_uri("Exponentiation")))

            # shortnames
            hasBase = PDF.set_uri("hasBase")
            hasExponent = PDF.set_uri("hasExponent")

            # insert base and exponent
            graph, node = transform_to_graph(expression["exp"][0], PDF, graph, symbols)
            graph.add((expr_node, hasBase, node))
            graph.add((expr_node, hasExponent, Literal(expression["exp"][1])))

        else:
            raise ValueError(
                f"Unrecognized keys in expression-object: {expression.keys()}."
            )

    else:
        raise ValueError(
            f"Expecting either a string or dict. Got '{type(expression)}'."
        )

    return graph, expr_node


def insert_unit_expr(g, txt_expression, PDF, syntax_type="inOtherSIUnits"):
    # define syntax style
    if syntax_type == "inOtherSIUnits":
        sx = {
            "division": "/",
            "times": "\\;",
            "exponent": "\^[-0-9]+",
            "exp_number": "\^([-0-9]+)",
            "variable": "@[a-z]+@",
            "var_name": "@([a-z]+)@",
        }

    elif syntax_type == "inBaseSIUnits":
        # TODO: untested
        sx = {
            "division": "/",  # not used
            "times": "\\;",
            "exponent": "\^[\{]?[-0-9]+[\}]?",
            "exp_number": "\^[\{]?([-0-9]+)[\}]?",
            "variable": "\{@[a-z]+@\}",
            "var_name": "\{@([a-z]+)@\}",
        }

    else:
        ValueError(f"Unknown syntax type '{syntax_type}'.")

    # parse txt into fragments
    expression_atoms = re.compile(
        f'({sx["variable"]}|{sx["division"]}|{sx["times"]}|{sx["exponent"]})'
    )
    fragments = re.findall(expression_atoms, txt_expression)

    # extract factors / division / exponents from fragments
    expression = parse_fragments(fragments, syntax=sx)

    # transform into RDF triples via lookup from symbols
    with open(os.path.join(CUQ_FILES_FOLDER, "symbols.yaml"), encoding="utf8") as fp:
        symbols = yaml.safe_load(fp)
    g, node = transform_to_graph(expression, PDF, graph=g, symbols=symbols)

    # print(txt_expression)
    # print(expression)
    # print("=" * 30)

    return g, node


def main():
    # import CUQ TBox
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
                    g.add(
                        (
                            element,
                            PDF.set_uri("hasPrefix"),
                            PDF.set_prefix_uri(dc["hasPrefix"]),
                        )
                    )
                if "hasBaseUnit" in dc.keys():
                    g.add(
                        (
                            element,
                            PDF.set_uri("hasBaseUnit"),
                            PDF.set_unit_uri(dc["hasBaseUnit"]),
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
            g.add(
                (element, PDF.hasUnitTypeAsString, Literal("SI base unit", lang="en"))
            )
            g.add(
                (
                    element,
                    PDF.hasUnitTypeAsString,
                    Literal("Unité SI de base", lang="fr"),
                )
            )
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
                            sf.formattxt(bdef["hasDefiningText_fr"], "latex"), lang="fr"
                        ),
                    )
                )
            if bdef["hasDefiningText_en"] is not None:
                g.add(
                    (
                        element,
                        PDF.hasDefiningText,
                        Literal(
                            sf.formattxt(bdef["hasDefiningText_en"], "latex"), lang="en"
                        ),
                    )
                )
            g.add(
                (
                    element,
                    PDF.hasDefiningResolution,
                    URIRef(PDF.set_cgpm_uri(bdef["hasDefiningResolution"])),
                )
            )
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
                            Literal(sf.formattxt(note["note_en"], "latex"), lang="en"),
                        )
                    )
                    g.add(
                        (
                            notenode,
                            PDF.hasNoteText,
                            Literal(sf.formattxt(note["note_fr"], "latex"), lang="fr"),
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
                    Literal(sf.formattxt(sisp["Symbol"], "latex"), datatype=XSD.string),
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

            if sisp["inOtherSIUnits"]:
                g, node = insert_unit_expr(
                    g, sisp["inOtherSIUnits"], PDF, "inOtherSIUnits"
                )
                g.add((element, PDF.inOtherSIUnits, node))
                tmp = sf.formattxt(sisp["inOtherSIUnits"], "latex", add_delim=False)
                g.add((node, RDFS.comment, Literal(tmp, datatype=XSD.string)))

            if sisp["inBaseSIUnits"]:
                g, node = insert_unit_expr(
                    g, sisp["inBaseSIUnits"], PDF, "inBaseSIUnits"
                )
                g.add((element, PDF.inBaseSIUnits, node))
                tmp = sf.formattxt(sisp["inBaseSIUnits"], "latex", add_delim=False)
                g.add((node, RDFS.comment, Literal(tmp, datatype=XSD.string)))

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
                    Literal(sf.formattxt(nsi["Symbol"], "latex"), datatype=XSD.string),
                )
            )
            g.add(
                (
                    element,
                    PDF.isUnitOfQtyKind,
                    PDF.set_quantity_uri(nsi["UnitOfQtyKind"]),
                )
            )
            g.add(
                (
                    element,
                    PDF.hasConversionFactor,
                    Literal(nsi["ConversionFactor"], datatype=XSD.double),
                )
            )
            g.add(
                (
                    element,
                    PDF.hasConversionUnit,
                    PDF.set_unit_uri(nsi["ConversionUnit"]),
                )
            )
    return g


if __name__ == "__main__":
    main()
