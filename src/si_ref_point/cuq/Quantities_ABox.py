#
# Quantities ABox
#

from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER, APIPATH
import yaml
import os


def main():
    PDF = SiElements()
    g = Graph()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(PDF.namespace_quantities), RDF.type, OWL.Ontology))
    g.add((URIRef(PDF.namespace_quantities), SKOS.prefLabel,
           Literal("SI Reference Point - Quantities", datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_quantities), RDFS.comment,
           Literal("Ontology, part of the SI reference point, "
                   "covering quantities",
                   datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_quantities), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # crawl through the items of the YAML file
    with open(os.path.join(CUQ_FILES_FOLDER, 'quantities.yaml')) as fp:
        qty_list = yaml.safe_load(fp)
    for qty in qty_list:
        element = PDF.set_quantity_uri(qty['identifier'])
        g.add((element, RDF.type, PDF.QuantityKind))
        g.add((element, SKOS.prefLabel,
               Literal(qty['quantity-en'], lang="en")))
        g.add((element, SKOS.prefLabel,
               Literal(qty['quantity-fr'], lang="fr")))
        g.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                               datatype=XSD.string)))
        if 'Unit' in qty and qty['Unit'] is not None:
            g.add((element, PDF.hasUnit, PDF.set_unit_uri(qty['Unit'])))
    g.serialize(format='turtle', destination=APIPATH + 'quantities.ttl')


if __name__ == "__main__":
    main()
