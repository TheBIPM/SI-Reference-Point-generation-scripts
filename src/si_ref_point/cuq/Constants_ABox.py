"""
constants A-Box
"""

from datetime import date
import os
from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Literal
import yaml
from si_ref_point.cuq.cuq_tbox import SiElements
import si_ref_point.cuq.symbols_format as sf
from si_ref_point.settings import CUQ_FILES_FOLDER
from si_ref_point.cuq.units_abox import transform_to_graph


def main():
    """ main of constants A-Box"""
    si_graph = SiElements()

    # 1) Annotations to the ontology (name, creation date, comment)
    si_graph.g.add((URIRef(si_graph.namespace_constants), RDF.type, OWL.Ontology))

    si_graph.g.add(
        (
            URIRef(si_graph.namespace_constants),
            SKOS.prefLabel,
            Literal("SI Reference Point - Constants", datatype=XSD.string)
       )
       )

    si_graph.g.add(
        (
            URIRef(si_graph.namespace_constants),
            DCTERMS.created,
            Literal(str(date.today()), datatype=XSD.date)
       )
       )

    si_graph.g.add(
        (
            URIRef(si_graph.namespace_constants),
            RDFS.comment,
            Literal(("Ontology, part of the SI reference point, covering the "
                    "seven underpinning constants of the SI"),
                   datatype=XSD.string)
       )
       )


    # 3) open yaml with information
    with open(os.path.join(CUQ_FILES_FOLDER,  'si_constants.yaml'),
              encoding="utf8") as fp:
        cst_list = yaml.safe_load(fp)

    for cst in cst_list:
        element = si_graph.set_constant_uri(cst['id'])
        si_graph.g.add((element, RDF.type, si_graph.constant))
        si_graph.g.add((element, si_graph.has_value_as_string,
               Literal(cst['value_str'], datatype=XSD.string)))
        # Deprecated in favor of "combined units" style
        # si_graph.g.add((element, si_graph.hasUnitAsString,
        #       Literal(cst['unit_str'], datatype=XSD.string)))
        if 'unit' in cst and cst['unit'] is not None:
            if isinstance(cst['unit'], list):
                # Transform into dict
                cmpnd_unit = {"mult": []}
                for item in cst['unit']:
                    cmpnd_unit['mult'].append({"exp": [item[0], item[1]]})
                si_graph.g, cmpnd_node = transform_to_graph(cmpnd_unit, si_graph, si_graph.g)
                si_graph.g.add((element, si_graph.has_unit, cmpnd_node))
            else:
                si_graph.g.add((element, si_graph.has_unit, si_graph.set_unit_uri(cst['unit'])))
        si_graph.g.add((element, si_graph.has_value,
               Literal(cst['value'], datatype=XSD[cst['xsd_type']], normalize=False)))
        si_graph.g.add((element, si_graph.has_datatype, XSD[cst['xsd_type']]))
        # note on xsd:double :
        # RDFLib has a known bug that loses precision in value for xsd:double
        # https://github.com/RDFLib/rdflib/issues/1852
        # xsd:float should be preferred

        latex_symbol = sf.formattxt(cst['symbol'], 'latex')
        si_graph.g.add((element, si_graph.has_symbol,
               Literal(latex_symbol, datatype=XSD.string)))
        si_graph.g.add((element, si_graph.has_updated_date,
               Literal(cst['updateddate'], datatype=XSD.date)))
        si_graph.g.add((element, SKOS.prefLabel,
               Literal(cst['name_en'], lang="en")))
        si_graph.g.add((element, SKOS.prefLabel,
               Literal(cst['name_fr'], lang="fr")))
        si_graph.g.add((element, SKOS.hiddenLabel,
               Literal(cst['hidden_label'], datatype=XSD.string)))
        si_graph.g.add((element, si_graph.has_defining_resolution,
               si_graph.set_cgpm_uri(cst['hasDefiningResolution'])))

    return si_graph.g


if __name__ == "__main__":
    main()
