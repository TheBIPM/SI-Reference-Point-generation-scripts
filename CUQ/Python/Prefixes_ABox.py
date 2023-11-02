#
# Prefixes ABox
#
#
# the module imports the Python script 'settings.py' located in a directory above this directory
# Should this lead to an error when executing the present script (... not found ...) you might need
# to add the location to the PYTHONPATH by typing (in the TERMINAL where you execute the Python script)
# export PYTHONPATH=(path where the package is located) (e.g. /Users/gregordudle/Development/Semantic-SI)
#

from rdflib import *
from CUQ_TBox import SiElements
from datetime import date
from settings import *
import yaml
import re
import os

# import CUQ TBox
PDF = SiElements()
g = Graph()

# copy over all namespaces from PDF.g to g
for key, val in PDF.g.namespaces():
    g.bind(key, val)

# Annotations to the ontology (name, Version number)
g.add((URIRef(PDF.namespace_prefixes), RDF.type, OWL.Ontology))
g.add((URIRef(PDF.namespace_prefixes), SKOS.prefLabel, Literal("SI Reference Point - Prefixes", datatype=XSD.string)))
g.add((URIRef(PDF.namespace_prefixes), RDFS.comment, Literal("Ontology, part of the SI Reference Point, covering "
                                                             "prefixes for the SI measurement units.")))
g.add((URIRef(PDF.namespace_prefixes), DCTERMS.created, Literal(str(date.today()), datatype=XSD.date)))

# 1) open YAML files with information
with open(os.path.join(XLS_FILES_FOLDER, 'prefixes.yaml')) as fp:
    prefixes = yaml.safe_load(fp)

# 2) Create prefixes
for prfx in prefixes:
    uri_text = prfx['URI']
    prefLabel_en = prfx['prefLabel_en']
    prefLabel_fr = prfx['prefLabel_fr']
    scalingFactor = prfx['ScalingFactor']
    symbol = prfx['hasSymbol']
    defres = prfx['hasDefiningResolution']
    try:
        datatype = prfx['datatype']
    except KeyError:
        import ipdb;ipdb.set_trace()  # noqa

    if uri_text is not None:
        element = PDF.set_prefix_uri(uri_text)
        g.add((element, RDF.type, PDF.SIPrefix))
        g.add((element, SKOS.prefLabel, Literal(prefLabel_fr, lang='fr')))
        g.add((element, SKOS.prefLabel, Literal(prefLabel_en, lang='en')))
        if datatype == "integer":
            g.add((element, PDF.hasScalingFactor, Literal(scalingFactor, datatype=XSD.integer)))
            g.add((element, PDF.hasDatatype, XSD.integer))
        elif datatype == "decimal":
            g.add((element, PDF.hasScalingFactor, Literal(scalingFactor, datatype=XSD.decimal)))
            g.add((element, PDF.hasDatatype, XSD.decimal))
        elif datatype == "float":
            g.add((element, PDF.hasScalingFactor, Literal(scalingFactor, datatype=XSD.float)))
            g.add((element, PDF.hasDatatype, XSD.float))
        g.add((element, PDF.hasSymbol, Literal(symbol, datatype=XSD.string)))
        g.add((element, PDF.hasDefiningResolution, URIRef(PDF.set_cgpm_uri(defres))))

# 5) Serialization prefixes
g.serialize(format='turtle', destination=APIPATH + 'prefixes.ttl')
