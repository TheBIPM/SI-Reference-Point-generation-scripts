"""
Quantities ABox
"""

from datetime import date
from time import time
import git
import os
import logging
from rdflib import Graph, RDF, OWL, URIRef, RDFS, DCTERMS, Literal, SKOS, XSD, PROV
import yaml
#from si_ref_point.cuq.cuq_tbox import SiElements   # as example if package is installed
from si_ref_point.cuq.cuq_tbox import SiElements
from si_ref_point.cuq.units_abox import transform_to_graph
from si_ref_point.settings import CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, CUQ_FILES_FOLDER, GITHUB_BASE_PATH, SIDFWBASE


def main():
    """Main of Quantities A-box"""
     # get the predicates and classes that are common to all cuq files
    si_graph = SiElements() 
    # produce a separate graphe for the units   
    quantities_graph = Graph()  

    # 1) Define the namespaces within (base)/SI
    quantities_graph.bind("quantities",si_graph.namespace_quantities)
    quantities_graph.bind("units",si_graph.namespace_units)
    quantities_graph.bind("si",si_graph.namespace)

    # 2) Add annotations to the quantity graph
    
    # 2.1 General annotations (type, labels, comments etc)

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
         RDFS.comment,
         Literal("Ontology, part of the SI reference point, "
                   "covering quantities",
                   datatype=XSD.string))
    )
    
    # 2.2 Versioning (using PROVENANCE vocabulary)
    timestamp = str(int(time()))
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    #   2.2.1 Agent
    #   declare this code as an 'agent' (in the sense of PROVENANCE)
    #   and define UàRI to a specific version by using its commit on github
    agents = []
    agents.append(GITHUB_BASE_PATH +"blob/"+ sha + "/src/si_ref_point/cuq/cuq_tbox.py")
    agents.append(GITHUB_BASE_PATH +"blob/"+ sha + "/src/si_ref_point/cuq/quantities_abox.py")

    for agent_sw in agents:
        quantities_graph.add(
            (URIRef(agent_sw),
                RDF.type,
                PROV.Agent)
        )
        
    #   2.2.2 Entity
    #   declare the sources (YAML files) as 'entity' (in the sense of PROVENANCE)
    #   The manually produced YAML files are stored on GitHub. Their hexsha together
    #   with the path is used to define a unique URI for each file.
    source_files = []
    source_files.append(GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq_data/quantities_core.yaml")
    source_files.append(GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq_data/quantities_other.yaml")
    for source in source_files:
        quantities_graph.add(
            (URIRef(source),
             RDF.type,
             PROV.Entity)
        )
    quantities_out_entity ="quantities_" + timestamp + ".ttl"
    quantities_graph.add(
        (si_graph.set_entity_uri(quantities_out_entity),
         RDF.type,
         PROV.Entity)
    )
    
    #   2.2.3 Activity
    #     declare the constants_ttl_generation as 'activity' (in the sense of PROVENANCE)
    #     make the activity unique by adding the timestamp to the identifier of the activity
    activity = 'quantities_'+timestamp + '.ttl_generation'     
    
    quantities_graph.add(
        (si_graph.set_activity_uri(activity),
        RDF.type,
        PROV.Activity)
    )
    
    #   2.2.4 Relation activity, agent, entities
    #   activity - agent
    for agent_sw in agents:
        quantities_graph.add(
                (si_graph.set_activity_uri(activity),
                PROV.wasAssociatedWith,
                URIRef(agent_sw))
            )
    quantities_graph.add(
        (si_graph.set_activity_uri(activity),
            PROV.startedAtTime,
            Literal(str(date.today()), datatype=XSD.date))
    )
    #   output entity - source entities
    for source in source_files:
        quantities_graph.add(
            (si_graph.set_entity_uri(quantities_out_entity),
                PROV.wasDerivedFrom,
                URIRef(source))
    )
    #   output entity - agent
    for agent_sw in agents:
        quantities_graph.add(
            (si_graph.set_entity_uri(quantities_out_entity),
            PROV.wasAttributedTo,
            URIRef(agent_sw))
    )
    #   output entity - activity
    quantities_graph.add(
        (si_graph.set_entity_uri(quantities_out_entity),
         PROV.wasGeneratedBy,
         si_graph.set_activity_uri(activity))
    )
    
    # 2.3 Licence information
    quantities_graph.add(
         (URIRef(si_graph.namespace_quantities),
          DCTERMS.license,
          URIRef(CC_LICENCE))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_EN,lang="en"))
    )
    quantities_graph.add(
        (URIRef(si_graph.namespace_quantities),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_FR,lang="fr"))
    )
    
    # 3) Build quantity graph
    #  crawl through the list of YAML files
    qty_files = ['quantities_core.yaml', 'quantities_other.yaml']
    qty_code_list = []

    # open YAML files with information
    for filename in qty_files:
        with open(os.path.join(CUQ_FILES_FOLDER, filename), encoding="utf8") as fp:
            qty_list = yaml.safe_load(fp)

            # add the individual quantities to the graph
            for qty in qty_list["data"]:
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
