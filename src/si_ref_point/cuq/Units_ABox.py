"""
Units ABox
"""

from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os
import si_ref_point.cuq.symbols_format as sf


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
                g.add(
                    (
                        element,
                        PDF.inOtherSIUnits,
                        Literal(
                            sf.formattxt(
                                sisp["inOtherSIUnits"], "latex", add_delim=False
                            ),
                            datatype=XSD.string,
                        ),
                    )
                )
            if sisp["inBaseSIUnits"]:
                g.add(
                    (
                        element,
                        PDF.inBaseSIUnits,
                        Literal(
                            sf.formattxt(
                                sisp["inBaseSIUnits"], "latex", add_delim=False
                            ),
                            datatype=XSD.string,
                        ),
                    )
                )
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
