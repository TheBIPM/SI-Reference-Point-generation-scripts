"""
Quantities ABox
"""

from datetime import date
import os
import logging
from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD
import yaml
from si_ref_point.cuq.cuq_tbox import SiElements
from si_ref_point.cuq.units_abox import transform_to_graph
from si_ref_point.settings import CUQ_FILES_FOLDER



def main():
    """Main of Quantities A-box"""
    si_graph = SiElements()
    g = Graph()

    # 1) copy over all namespaces from si_graph.g to g
    for key, val in si_graph.g.namespaces():
        g.bind(key, val)

    # 2) add annotations to the ontology (name, creation date, comment)
    g.add((URIRef(si_graph.namespace_quantities), RDF.type, OWL.Ontology))
    g.add(
        (
            URIRef(si_graph.namespace_quantities),
            SKOS.prefLabel,
            Literal("SI Reference Point - Quantities", datatype=XSD.string)
        )
    )

    g.add(
        (
            URIRef(si_graph.namespace_quantities), DCTERMS.created,
            Literal(str(date.today()), datatype=XSD.date)
        )
    )

    g.add(
        (
            URIRef(si_graph.namespace_quantities), RDFS.comment,
            Literal("Ontology, part of the SI reference point, "
                   "covering quantities",
                   datatype=XSD.string)
        )
    )
    # 3) crawl through the list of YAML files
    qty_files = ['quantities_core.yaml', 'quantities_other.yaml']
    qty_code_list = []

    # 4) open YAML files with information
    for filename in qty_files:
        with open(os.path.join(CUQ_FILES_FOLDER, filename), encoding="utf8") as fp:
            qty_list = yaml.safe_load(fp)

            # add the individual quantities to the graph
            for qty in qty_list:
                if qty['identifier'] not in qty_code_list:
                    qty_code_list.append(qty['identifier'])
                else:
                    logging.error("quantity %s already defined !", qty['identifier'] )
                element = si_graph.set_quantity_uri(qty['identifier'])
                g.add((element, RDF.type, si_graph.quantity_kind))
                g.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-en'], lang="en")))
                g.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-fr'], lang="fr")))
                g.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                                       datatype=XSD.string)))
                if 'Unit' in qty and qty['Unit'] is not None:
                    g, cmpnd_node = transform_to_graph(qty['Unit'], si_graph, g)
                    g.add((element, si_graph.has_unit, cmpnd_node))

    return g

if __name__ == "__main__":
    main()
