"""
Prefixes ABox
"""
from datetime import datetime, timezone
import git
import os
import yaml
from rdflib import Graph, URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Literal, PROV
from si_ref_point.tboxes.si_tbox import SiElements
from si_ref_point.settings import CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, SI_FILES_FOLDER, GITHUB_BASE_PATH


def main():
    """main of Prefixes A-box"""

    # get the predicates and classes that are common to all cuq files
    si_graph = SiElements()
    # produce a separate graph for the prefixes
    prefix_graph = Graph()      

    # 1) Define the namespaces within (base)/SI
    prefix_graph.bind("prefixes",si_graph.namespace_prefixes)
    prefix_graph.bind("si",si_graph.namespace)

    # 2) Annotations to the prefix-graph
    
    # 2.1 General annotations (type, labels, comments etc)
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         RDF.type,
         OWL.Ontology)
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         SKOS.prefLabel,
         Literal("SI Reference Point - Prefixes", datatype=XSD.string))
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         RDFS.comment,
         Literal("Ontology, part of the SI Reference Point, covering "
                   "prefixes for the SI measurement units."))
    )

    # 2.2 Versioning (using PROVENANCE vocabulary)
    timestamp = datetime.now(timezone.utc)                              # get the system time (in UTC)
    uri_timestamp = timestamp.strftime("%Y%m%d%H%M%SZ")                 # used to identify uniquely the produced TTL file (entity)
    startedAt_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")      # used with the predicate 'startedAtTime' of the corresponding activity
    
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    
    #     2.2.1 Agent
    #     declare this code as an 'agent' (in the sense of PROVENANCE) 
    #     and define URI to a specific version by using the commit reference on GitHub
    agents = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/prefixes_abox.py",
              GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/cuq/si_tbox.py"]
    for agent in agents:
        prefix_graph.add(
            (URIRef(agent),
                RDF.type,
                PROV.Agent)
        )

    #     2.2.2 Entity
    #     declare the source (YAML file) as 'entity' (in the sense of PROVENANCE)
    #     The manually produced YAML files are stored on GITHUB. Their hexsha together
    #     with the path are used as a unique identifier
    source_list = [GITHUB_BASE_PATH + "blob/" + sha + "/src/si_ref_point/si/prefixes.yaml"]
    for source in source_list:
        prefix_graph.add(
            (URIRef(source),
                RDF.type,
                PROV.Entity)
        )

    #     declare the ttl output as an 'entity' (in the sense of PROVENANCE)
    #     make the entity unique by adding the timestamp to the identifier of the output file
    prefix_out_entity = "prefixes_"+uri_timestamp+".ttl"
    prefix_graph.add(
        (si_graph.set_entity_uri(prefix_out_entity),
            RDF.type,
            PROV.Entity)
    )
        
    #     2.2.3 Activity    
    #     declare the prefixes_ttl_generation as 'activity' (in the sense of PROVENANCE)
    #     make the activity unique by adding the timestamp to the identifier of the activity
    activity = 'prefixes_'+ uri_timestamp +'.ttl_generation'
    prefix_graph.add(
        (si_graph.set_activity_uri(activity),
        RDF.type,
        PROV.Activity)
    )
    
    #     2.2.4 Link activity, agent, entities
    #     activity - agent
    for agent in agents:
        prefix_graph.add(
            (si_graph.set_activity_uri(activity),
            PROV.wasAssociatedWith,
            URIRef(agent))
        )
    prefix_graph.add(
        (si_graph.set_activity_uri(activity),
            PROV.startedAtTime,
            Literal(str(startedAt_timestamp), datatype=XSD.dateTime))
    )
    #    output entity - source entities
    for source in source_list:
        prefix_graph.add(
            (si_graph.set_entity_uri(prefix_out_entity),
                PROV.wasDerivedFrom,
                URIRef(source))
        )
        #    output entity - agent
    for agent in agents:
        prefix_graph.add(
            (si_graph.set_entity_uri(prefix_out_entity),
                PROV.wasAttributedTo,
                URIRef(agent))
        )
    #    output entity - activity
    prefix_graph.add(
        (si_graph.set_entity_uri(prefix_out_entity),
            PROV.wasGeneratedBy,
            si_graph.set_activity_uri(activity))
    )
    
    # 2.3 Licence
    prefix_graph.add(
         (URIRef(si_graph.namespace_prefixes),
          DCTERMS.license,
          URIRef(CC_LICENCE))
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_EN,lang="en"))
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         RDFS.comment,
         Literal(CC_LICENCE_TEXT_FR,lang="fr"))
    )
    
    # 3) Build prefix graph
    
    # 3.1 Open YAML files as source
    with open(os.path.join(SI_FILES_FOLDER, 'prefixes.yaml'),encoding='utf-8') as fp:
        prefixes = yaml.safe_load(fp)

    # 3.2 Fill graph with all prefix entries
    for prfx in prefixes["data"]:
        uri_text = prfx['URI']
        pref_label_en = prfx['prefLabel_en']
        pref_label_fr = prfx['prefLabel_fr']
        scaling_factor = prfx['ScalingFactor']
        exponent = prfx['Exponent']
        symbol = prfx['hasSymbol']
        defres = prfx['hasDefiningResolution']
        xsd_type = prfx['xsd_type']


        if uri_text is not None:
            element = si_graph.set_prefix_uri(uri_text)
            prefix_graph.add((element, RDF.type, si_graph.si_prefix))
            prefix_graph.add((element, SKOS.prefLabel, Literal(pref_label_fr, lang='fr')))
            prefix_graph.add((element, SKOS.prefLabel, Literal(pref_label_en, lang='en')))
            prefix_graph.add((element, si_graph.has_scaling_factor,
                Literal(scaling_factor, datatype=XSD[xsd_type], normalize=False)))
            prefix_graph.add((element, si_graph.has_datatype, XSD[xsd_type]))
            prefix_graph.add(
                (
                    element,
                    si_graph.has_exponent,
                    Literal(exponent,datatype=XSD['integer'])
                )
            )

            if symbol:
                prefix_graph.add((element, si_graph.has_symbol,
                   Literal(symbol, datatype=XSD.string)))

            if defres:
                prefix_graph.add((element, si_graph.has_defining_resolution,
                     URIRef(si_graph.set_cgpm_uri(defres))))

    return prefix_graph
