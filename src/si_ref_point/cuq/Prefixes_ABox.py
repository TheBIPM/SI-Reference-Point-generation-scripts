#
# Prefixes ABox

from rdflib import URIRef, RDF, OWL, SKOS, XSD, RDFS, DCTERMS, Graph, Literal
from si_ref_point.cuq.CUQ_TBox import SiElements
from datetime import date
from si_ref_point.settings import CUQ_FILES_FOLDER
import yaml
import os


def main():
    PDF = SiElements()
    g = Graph()

    # copy over all namespaces from PDF.g to g
    for key, val in PDF.g.namespaces():
        g.bind(key, val)

    # Annotations to the ontology (name, Version number)
    g.add((URIRef(PDF.namespace_prefixes), RDF.type, OWL.Ontology))
    g.add((URIRef(PDF.namespace_prefixes), SKOS.prefLabel,
           Literal("SI Reference Point - Prefixes", datatype=XSD.string)))
    g.add((URIRef(PDF.namespace_prefixes), RDFS.comment,
           Literal("Ontology, part of the SI Reference Point, covering "
                   "prefixes for the SI measurement units.")))
    g.add((URIRef(PDF.namespace_prefixes), DCTERMS.created,
           Literal(str(date.today()), datatype=XSD.date)))

    # 1) open YAML files with information
    with open(os.path.join(CUQ_FILES_FOLDER, 'prefixes.yaml')) as fp:
        prefixes = yaml.safe_load(fp)

    # 2) Create prefixes
    for prfx in prefixes:
        uri_text = prfx['URI']
        prefLabel_en = prfx['prefLabel_en']
        prefLabel_fr = prfx['prefLabel_fr']
        scalingFactor = prfx['ScalingFactor']
        symbol = prfx['hasSymbol']
        defres = prfx['hasDefiningResolution']
        xsd_type = prfx['xsd_type']

        if uri_text is not None:
            element = PDF.set_prefix_uri(uri_text)
            g.add((element, RDF.type, PDF.SIPrefix))
            g.add((element, SKOS.prefLabel, Literal(prefLabel_fr, lang='fr')))
            g.add((element, SKOS.prefLabel, Literal(prefLabel_en, lang='en')))
            g.add((element, PDF.hasScalingFactor,
                Literal(scalingFactor, datatype=XSD[xsd_type], normalize=False)))
            g.add((element, PDF.hasDatatype, XSD[xsd_type]))

            if symbol:
                g.add((element, PDF.hasSymbol,
                   Literal(symbol, datatype=XSD.string)))

            if defres:
                g.add((element, PDF.hasDefiningResolution,
                     URIRef(PDF.set_cgpm_uri(defres))))

    return g
