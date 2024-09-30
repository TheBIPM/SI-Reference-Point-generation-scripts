"""
Constants ABox
"""

from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal
from si_ref_point.cuq.CUQ_TBox import SiElements
import si_ref_point.cuq.symbols_format as sf
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
from si_ref_point.cuq.Units_ABox import transform_to_graph
import yaml
import os


def main():
    PDF = SiElements()
    g = Graph()

    # 1) copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # 2) Annotations to the ontology (name, creation date, comment)
    g.add((URIRef(PDF.namespace_constants), RDF.type, OWL.Ontology))
 
    g.add(
        (
            URIRef(PDF.namespace_constants), 
            SKOS.prefLabel,
            Literal("SI Reference Point - Constants", datatype=XSD.string)
       )
       )
    
    g.add(
        (
            URIRef(PDF.namespace_constants),
            DCTERMS.created,
            Literal(str(date.today()), datatype=XSD.date)
       )
       )
    
    g.add(
        (
            URIRef(PDF.namespace_constants),
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
        element = PDF.set_constant_uri(cst['id'])
        g.add((element, RDF.type, PDF.Constant))
        g.add((element, PDF.hasValueAsString,
               Literal(cst['value_str'], datatype=XSD.string)))
        # Deprecated in favor of "combined units" style
        # g.add((element, PDF.hasUnitAsString,
        #       Literal(cst['unit_str'], datatype=XSD.string)))
        if 'unit' in cst and cst['unit'] is not None:
            if isinstance(cst['unit'], list):
                # Transform into dict
                cmpnd_unit = {"mult": []}
                for item in cst['unit']:
                    cmpnd_unit['mult'].append({"exp": [item[0], item[1]]})
                g, cmpnd_node = transform_to_graph(cmpnd_unit, PDF, g)
                g.add((element, PDF.hasUnit, cmpnd_node))
            else:
                g.add((element, PDF.hasUnit, PDF.set_unit_uri(cst['unit'])))
        g.add((element, PDF.hasValue,
               Literal(cst['value'], datatype=XSD[cst['xsd_type']], normalize=False)))
        g.add((element, PDF.hasDatatype, XSD[cst['xsd_type']]))
        # note on xsd:double :
        # RDFLib has a known bug that loses precision in value for xsd:double
        # https://github.com/RDFLib/rdflib/issues/1852
        # xsd:float should be preferred

        latex_symbol = sf.formattxt(cst['symbol'], 'latex')
        g.add((element, PDF.hasSymbol,
               Literal(latex_symbol, datatype=XSD.string)))
        g.add((element, PDF.hasUpdatedDate,
               Literal(cst['updateddate'], datatype=XSD.date)))
        g.add((element, SKOS.prefLabel,
               Literal(cst['name_en'], lang="en")))
        g.add((element, SKOS.prefLabel,
               Literal(cst['name_fr'], lang="fr")))
        g.add((element, SKOS.hiddenLabel,
               Literal(cst['hidden_label'], datatype=XSD.string)))
        g.add((element, PDF.hasDefiningResolution,
               PDF.set_cgpm_uri(cst['hasDefiningResolution'])))

    return g


if __name__ == "__main__":
    main()
