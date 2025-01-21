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
    si_graph = SiElements()     # get the predicates and classes that are common to all cuq files
    quantities_graph = Graph()  # produce a separate graphe for the units

    # Define the namespaces within (base)/SI
    quantities_graph.bind("quantities",si_graph.namespace_quantities)
    quantities_graph.bind("units",si_graph.namespace_units)
    quantities_graph.bind("si",si_graph.namespace)


    # 1) Add annotations to the ontology

    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDF.type,
         OWL.Ontology)
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         SKOS.prefLabel,
         Literal("SI Reference Point - Quantities", datatype=XSD.string))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         DCTERMS.created,
         Literal(str(date.today()), datatype=XSD.date))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal("Ontology, part of the SI reference point, "
                   "covering quantities",
                   datatype=XSD.string))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         OWL.versionIRI,
         URIRef("https://si-digital-framework.org/SI/releases/2024-12-17/quantities.ttl"))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         OWL.versionInfo,
         Literal('2024-12-17',datatype=XSD.string))
    )
    # 2) crawl through the list of YAML files
    qty_files = ['quantities_core.yaml', 'quantities_other.yaml']
    qty_code_list = []

    # 3) open YAML files with information
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
                quantities_graph.add((element, RDF.type, si_graph.quantity_kind))
                quantities_graph.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-en'], lang="en")))
                quantities_graph.add((element, SKOS.prefLabel,
                       Literal(qty['quantity-fr'], lang="fr")))
                quantities_graph.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                                       datatype=XSD.string)))
                if 'Unit' in qty and qty['Unit'] is not None:
                    quantities_graph, cmpnd_node = transform_to_graph(qty['Unit'], si_graph, quantities_graph)
                    quantities_graph.add((element, si_graph.has_unit, cmpnd_node))

    return quantities_graph

if __name__ == "__main__":
    main()
