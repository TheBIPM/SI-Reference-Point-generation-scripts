"""
Prefixes ABox
"""


import os
from datetime import date
import yaml
from rdflib import Graph, URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Literal, PROV
from si_ref_point.cuq.cuq_tbox import SiElements
from si_ref_point.settings import CC_LICENCE, CC_LICENCE_TEXT_EN, CC_LICENCE_TEXT_FR, CUQ_FILES_FOLDER,GENERATING_SW_VERSION,RELEASE_DATE, SIDFWBASE


def main():
    """main of Prefixes A-box"""

    si_graph = SiElements()     # get the predicates and classes that are common to all cuq files
    prefix_graph = Graph()      # produce a separate graphe for the prefixes

    # Define the namespaces within (base)/SI
    prefix_graph.bind("prefixes",si_graph.namespace_prefixes)
    prefix_graph.bind("si",si_graph.namespace)

    # Add annotations to the ontology

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
         DCTERMS.created,
         Literal(str(date.today()), datatype=XSD.date))
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         RDFS.comment,
         Literal("Ontology, part of the SI Reference Point, covering "
                   "prefixes for the SI measurement units."))
    )
    version_iri_path = SIDFWBASE + "/SI/releases/"+RELEASE_DATE+"/prefixes.ttl"
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         OWL.versionIRI,
         URIRef(version_iri_path))
    )
    prefix_graph.add(
        (URIRef(si_graph.namespace_prefixes),
         PROV.wasGeneratedBy,
         Literal(GENERATING_SW_VERSION,datatype=XSD.string))
    )
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
    # 1) open YAML files with information
    with open(os.path.join(CUQ_FILES_FOLDER, 'prefixes.yaml'),encoding='utf-8') as fp:
        prefixes = yaml.safe_load(fp)

    # 2) Create prefixes
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
