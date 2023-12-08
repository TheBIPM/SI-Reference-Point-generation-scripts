import owlrl
import rdflib
from rdflib import OWL, RDF, RDFS
import io
from owlready2 import World, sync_reasoner_pellet, sync_reasoner_hermit

# script parameters
do_RDFS_completion = True  # infer rdfs hierarchies
do_OWLRL_completion = True  # rule based semantics reasoner
do_OWLDL_completion = (
    not do_OWLRL_completion  # direct semantics reasoner, HermiT/Pellet is used
)
do_OWLDL_with_Pellet = True 

knowledge_bases = {
    #"test": {"path": "testing.ttl", "format": "ttl"},
    "si_base": {"path": "build/si.ttl", "format": "ttl"},
    "units": {"path": "build/units.ttl", "format": "ttl"},
    "quantities": {"path": "build/quantities.ttl", "format": "ttl"},
    "prefixes": {"path": "build/prefixes.ttl", "format": "ttl"},
    "constants": {"path": "build/constants.ttl", "format": "ttl"},
    "examples": {"path": "examples.ttl", "format": "ttl"},
}


# load them into rdflib-graph
g_rdf = rdflib.Graph()
for kb, kb_val in knowledge_bases.items():
    g_rdf.parse(kb_val["path"], format=kb_val["format"])

if do_RDFS_completion:
    # add rdfs triples, as Pellet/HermiT does not seem to make that explicit
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, improved_datatypes=False).expand(
        g_rdf
    )  # RDFS_OWLRL_Semantics

    # remove injected rdfs:Resource types (otherwise Pellet reasoner throws warnings)
    for s, p, o in g_rdf.triples((None, RDF.type, RDFS.Resource)):
        g_rdf.remove((s, p, o))
    
    # remove injected rdf:Property (otherwise HermiT reasoner throws error)
    for s, p, o in g_rdf.triples((None, RDF.type, RDF.Property)):
        g_rdf.remove((s, p, o))

    # remove injected owl:sameAs triples (not of interest here)
    for s, p, o in g_rdf.triples((None, OWL.sameAs, None)):
        if s == o:
            g_rdf.remove((s, p, o))

if do_OWLRL_completion:
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics, improved_datatypes=False).expand(
        g_rdf
    )

if do_OWLDL_completion:
    # convert to owlready2 graph to enable reasoning with Pellet/HermiT
    graph_string = g_rdf.serialize(format="xml")
    f = io.BytesIO(graph_string.encode("utf8"))
    world = World()
    onto = world.get_ontology("").load(fileobj=f)
    f.close()

    # apply reasoner
    if do_OWLDL_with_Pellet:
        sync_reasoner_pellet(world, infer_property_values=False, debug=2)
    else:
        sync_reasoner_hermit(world, infer_property_values=True, debug=2)

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
    SELECT DISTINCT ?s ?o
    WHERE {
        ?s rdf:type/rdfs:subClassOf* ?o .
        ?s rdf:type/rdfs:subClassOf* si:MeasurementUnit .
    }
"""

qres = g_rdf.query(query_mu)
print("\nMeasurement units and all their inferred/known types:")
for row in qres:
    unit = row.s.n3(g_rdf.namespace_manager)
    val = row.o.n3(g_rdf.namespace_manager)

    print(f"{unit} --> {val}")


####################################
query_prefixed = """
    SELECT DISTINCT ?unit
    WHERE {
        ?unit rdf:type/rdfs:subClassOf* si:CompoundUnit .
    }
"""
print("\nCompound Units:")
for row in g_rdf.query(query_prefixed):
    unit = row.unit.n3(g_rdf.namespace_manager)
    print(unit)


####################################
query_prefixed = """
    SELECT DISTINCT ?unit
    WHERE {
        ?unit rdf:type si:PrefixedUnit .
    }
"""
print("\nPrefixed units:")
for row in g_rdf.query(query_prefixed):
    unit = row.unit.n3(g_rdf.namespace_manager)
    print(unit)


####################################
query_prefixed = """
    SELECT DISTINCT ?unit
    WHERE {
        ?unit rdf:type si:UnitMultiple .
    }
"""
print("\nUnit Multiples:")
for row in g_rdf.query(query_prefixed):
    unit = row.unit.n3(g_rdf.namespace_manager)
    print(unit)
