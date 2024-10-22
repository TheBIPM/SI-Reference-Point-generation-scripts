"""
Prefixes ABox
"""


import os
from datetime import date
import yaml
from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Literal
from si_ref_point.cuq.cuq_tbox import SiElements
from si_ref_point.settings import CUQ_FILES_FOLDER


def main():
    """main of Prefixes A-box"""
    si_graph = SiElements()


    # Annotations to the ontology (name, Version number)
    si_graph.g.add((URIRef(si_graph.namespace_prefixes), RDF.type, OWL.Ontology))
    si_graph.g.add((URIRef(si_graph.namespace_prefixes), SKOS.prefLabel,
           Literal("SI Reference Point - Prefixes", datatype=XSD.string)))
    si_graph.g.add((URIRef(si_graph.namespace_prefixes), RDFS.comment,
           Literal("Ontology, part of the SI Reference Point, covering "
                   "prefixes for the SI measurement units.")))
    si_graph.g.add((URIRef(si_graph.namespace_prefixes), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # 1) open YAML files with information
    with open(os.path.join(CUQ_FILES_FOLDER, 'prefixes.yaml'),encoding='utf-8') as fp:
        prefixes = yaml.safe_load(fp)

    # 2) Create prefixes
    for prfx in prefixes:
        uri_text = prfx['URI']
        pref_label_en = prfx['prefLabel_en']
        pref_label_fr = prfx['prefLabel_fr']
        scaling_factor = prfx['ScalingFactor']
        symbol = prfx['hasSymbol']
        defres = prfx['hasDefiningResolution']
        xsd_type = prfx['xsd_type']

        if uri_text is not None:
            element = si_graph.set_prefix_uri(uri_text)
            si_graph.g.add((element, RDF.type, si_graph.si_prefix))
            si_graph.g.add((element, SKOS.prefLabel, Literal(pref_label_fr, lang='fr')))
            si_graph.g.add((element, SKOS.prefLabel, Literal(pref_label_en, lang='en')))
            si_graph.g.add((element, si_graph.has_scaling_factor,
                Literal(scaling_factor, datatype=XSD[xsd_type], normalize=False)))
            si_graph.g.add((element, si_graph.has_datatype, XSD[xsd_type]))

            if symbol:
                si_graph.g.add((element, si_graph.has_symbol,
                   Literal(symbol, datatype=XSD.string)))

            if defres:
                si_graph.g.add((element, si_graph.has_defining_resolution,
                     URIRef(si_graph.set_cgpm_uri(defres))))

    return si_graph.g
