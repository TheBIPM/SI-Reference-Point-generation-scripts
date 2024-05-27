"""
Quantities ABox
"""

from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
from si_ref_point.cuq.CUQ_TBox import SiElements
from si_ref_point.cuq.Units_ABox import transform_to_graph
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os
import logging



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
    qty_files = ['quantities_core.yaml', 'quantities_other.yaml']
    qty_code_list = []
    for filename in qty_files:
        with open(os.path.join(CUQ_FILES_FOLDER, filename), encoding="utf8") as fp:
            qty_list = yaml.safe_load(fp)
            for qty in qty_list:
                if qty['identifier'] not in qty_code_list:
                    qty_code_list.append(qty['identifier'])
                else:
                    logging.error("quantity %s already defined !" % qty['identifier'])
                element = PDF.set_quantity_uri(qty['identifier'])
                g.add((element, RDF.type, PDF.QuantityKind))
                g.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-en'], lang="en")))
                g.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-fr'], lang="fr")))
                g.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                                       datatype=XSD.string)))
                if 'Unit' in qty and qty['Unit'] is not None:
                    g, cmpnd_node = transform_to_graph(qty['Unit'], PDF, g)
                    g.add((element, PDF.hasUnit, cmpnd_node))
    return g
