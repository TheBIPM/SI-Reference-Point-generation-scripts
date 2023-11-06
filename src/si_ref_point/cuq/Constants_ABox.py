#
# Constants ABox
#

from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal
from si_ref_point.cuq.CUQ_TBox import SiElements
import si_ref_point.cuq.symbols_format as sf
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os


def main():
    g = Graph()
    PDF = SiElements()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, creation date, comment)
    g.add((URIRef(PDF.namespace_constants), RDF.type, OWL.Ontology))
    g.add((URIRef(PDF.namespace_constants), SKOS.prefLabel,
           Literal("SI Reference Point - Constants", datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_constants), RDFS.comment,
           Literal(("Ontology, part of the SI reference point, covering the "
                    "seven underpinning constants of the SI"),
                   datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_constants), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # worksheet containing the basic information
    with open(os.path.join(CUQ_FILES_FOLDER,  'si_constants.yaml'),
              encoding="utf8") as fp:
        cst_list = yaml.safe_load(fp)

    for cst in cst_list:
        element = PDF.set_constant_uri(cst['id'])
        g.add((element, RDF.type, PDF.Constant))
        g.add((element, PDF.hasValueAsString,
               Literal(cst['value_str'], datatype=XSD.string)))
        g.add((element, PDF.hasUnitAsString,
               Literal(cst['unit_str'], datatype=XSD.string)))
        if cst['value_type'] == "xsd:integer":
            g.add((element, PDF.hasDatatype,  XSD.integer))
            g.add((element, PDF.hasValue,
                   Literal(cst['value'], datatype=XSD.integer,
                           normalize=False)))
        elif cst['value_type'] == "xsd:double":
            # changing the output datatype to xsd:float as RDFLib has a
            # known bug that loses precision in value
            # https://github.com/RDFLib/rdflib/issues/1852
            g.add((element, PDF.hasDatatype, XSD.float))
            g.add((element, PDF.hasValue,
                   Literal(cst['value'], datatype=XSD.float, normalize=False)))
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
