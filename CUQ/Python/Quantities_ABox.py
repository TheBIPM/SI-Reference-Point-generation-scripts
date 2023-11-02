#
# Quantities ABox
#
#
# the module imports the Python script 'settings.py' located in a directory above this directory
# Should this lead to an error when executing the present script (... not found ...) you might need
# to add the location to the PYTHONPATH by typing (in the TERMINAL where you execute the Python script)
# export PYTHONPATH=(path where the package is located) (e.g. /Users/gregordudle/Development/Semantic-SI)
#

from rdflib import URIRef, Literal, Graph
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, OWL, XSD
from CUQ_TBox import SiElements
from datetime import date
from settings import *
import yaml
import os


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
       Literal("Ontology, part of the SI reference point, covering quantities",
               datatype=XSD.string)))
g.add((URIRef(PDF.namespace_quantities), DCTERMS.created,
       Literal(str(date.today()), datatype=XSD.date)))

# crawl through the items of the YAML file
with open(os.path.join(XLS_FILES_FOLDER, 'quantities.yaml')) as fp:
    qty_list = yaml.safe_load(fp)
for qty in qty_list:
    element = PDF.set_quantity_uri(qty['identifier'])
    g.add((element, RDF.type, PDF.QuantityKind))
    g.add((element, SKOS.prefLabel, Literal(qty['quantity-en'], lang="en")))
    g.add((element, SKOS.prefLabel, Literal(qty['quantity-fr'], lang="fr")))
    g.add((element, SKOS.altLabel, Literal(qty['identifier'],
                                           datatype=XSD.string)))
    if 'Unit' in qty and qty['Unit'] is not None:
        g.add((element, PDF.hasUnit, PDF.set_unit_uri(qty['Unit'])))

g.serialize(format='turtle', destination=APIPATH + 'quantities.ttl')
