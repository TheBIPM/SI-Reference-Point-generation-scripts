import owlrl
import rdflib
from rdflib import OWL, RDF, RDFS
import io
from owlready2 import World, sync_reasoner_pellet

# script parameters
do_RDFS_completion = True  # infer rdfs hierarchies
do_OWLDL_completion = True  # direct semantics reasoner, Pellet is used
knowledge_bases = {
    # "test": {"path": "testing.ttl", "format": "ttl"},
    "si_base": {"path": "build/si.ttl", "format": "ttl"},
    "units": {"path": "build/units.ttl", "format": "ttl"},
    #"quantities": {"path": "build/quantities.ttl", "format": "ttl"},
    #"prefixes": {"path": "build/prefixes.ttl", "format": "ttl"},
    #"constants": {"path": "build/constants.ttl", "format": "ttl"},
    # "examples": {"path": "examples.ttl", "format": "ttl"},
}


# load them into rdflib-graph
g_rdf = rdflib.Graph()
for kb, kb_val in knowledge_bases.items():
    g_rdf.parse(kb_val["path"], format=kb_val["format"])

if do_RDFS_completion:
    # add rdfs triples, as Pellet/HermiT does not seem to make that explicit
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, improved_datatypes=False).expand(g_rdf)

    # remove injected rdfs:Resource types (otherwise Pellet reasoner throws warnings)
    for s, p, o in g_rdf.triples((None, RDF.type, RDFS.Resource)):
        g_rdf.remove((s, p, o))

if do_OWLDL_completion:
    # convert to owlready2 graph to enable reasoning with Pellet/HermiT
    graph_string = g_rdf.serialize(format="xml")
    f = io.BytesIO(graph_string.encode("utf8"))
    world = World()
    onto = world.get_ontology("").load(fileobj=f)
    f.close()

    # apply reasoner
    sync_reasoner_pellet(world, infer_property_values=False, debug=2)

    # show inconsistent classes
    print(list(world.inconsistent_classes()))

    # convert back to rdflib graph (and copy namespaces from original graph)
    g_rdf_reasoned = world.as_rdflib_graph()
    g_rdf_reasoned.namespace_manager = g_rdf.namespace_manager
    # print(g_rdf_reasoned.serialize(format="ttl"))

    # overwrite
    g_rdf = g_rdf_reasoned


####################################
query_mu = """
    SELECT ?s ?o
    WHERE {
        ?s rdf:type ?o .
        #?s rdf:type si:Definition .
        ?s rdf:type si:MeasurementUnit .
        #?s rdf:type si:SIPrefix .
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

    # if unit.startswith("ex:") or unit.startswith("_:") or unit == "units:kilogram" or unit == "units:gram":
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
