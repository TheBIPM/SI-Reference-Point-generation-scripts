import owlrl
import rdflib
from rdflib import OWL, RDF, RDFS

# where knowledge bases are stored
knowledge_bases = {
    "si_derived_additions": {"path": "CUQ/proposed_terminology_for_derived_UQD.ttl", "format": "ttl"},
    "si_base": {"path": "Testing/API/si.ttl", "format": "ttl"},
    "units": {"path": "Testing/API/units.ttl", "format": "ttl"},
    "quantities": {"path": "Testing/API/quantities.ttl", "format": "ttl"},
    "prefixes": {"path": "Testing/API/prefixes.ttl", "format": "ttl"},
} 

# load them into rdflib-graph
g_rdf = rdflib.Graph()
for kb, kb_val in knowledge_bases.items():
    g_rdf.parse(kb_val["path"], format=kb_val["format"])

# infer implicit triples by reasoning
owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g_rdf)

####################################
query_mu = """
    SELECT ?s ?o
    WHERE {
        ?s rdf:type ?o .
        ?s rdf:type si:MeasurementUnit .
    }
"""

qres = g_rdf.query(query_mu)
print("\nMeasurement units and their types:")
for row in qres:
    unit = row.s.n3(g_rdf.namespace_manager)
    val = row.o.n3(g_rdf.namespace_manager)

    print(f"{unit} --> {val}")

####################################
query_all = """
    SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o .
        ?s si:includesUseOf ?o .
        #?unit rdf:type ?val .
        #?unit rdf:type si:MeasurementUnit .
    }
"""

qres = g_rdf.query(query_all)
print("\nIncludes use of units:")
for row in qres:
    unit = row.s.n3(g_rdf.namespace_manager)
    prop = row.p.n3(g_rdf.namespace_manager)
    val = row.o.n3(g_rdf.namespace_manager)

    #if unit.startswith("ex:") or unit.startswith("_:") or unit == "units:kilogram" or unit == "units:gram":
    print(f"{unit} --> {prop} --> {val}")

####################################
query_prefixed = """
    SELECT ?unit
    WHERE {
        ?unit rdf:type si:PrefixedUnit .
    }
"""
print("\nPrefixed units:")
for row in g_rdf.query(query_prefixed):
    unit = row.unit.n3(g_rdf.namespace_manager)
    print(unit)

####################################
query_coherent = """
    SELECT ?unit
    WHERE {
        ?unit rdf:type si:StrictCoherentUnit .
    }
"""
print("\nCoherent units:")
for row in g_rdf.query(query_coherent):
    unit = row.unit.n3(g_rdf.namespace_manager)
    print(unit)

