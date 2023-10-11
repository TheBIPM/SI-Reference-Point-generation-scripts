import owlrl
import rdflib
from rdflib import OWL, RDF, RDFS
from rdflib.extras.external_graph_libs import rdflib_to_networkx_digraph

# where knowledge bases are stored
knowledge_bases = {
    "si_derived_additions": {"path": "CUQ/proposed_terminology_for_derived_UQD.ttl", "format": "ttl"},
    "si_base": {"path": "Testing/API/si.ttl", "format": "ttl"},
} 

# load them into rdflib-graph
g_rdf = rdflib.Graph()
for kb, kb_val in knowledge_bases.items():
    g_rdf.parse(kb_val["path"], format=kb_val["format"])

# infer implicit triples by reasoning
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g_rdf)

# remove owl:sameAs relations, if they only cover identity
for subj, pred, obj in g_rdf.triples((None, None, None)):

    if "nanosecond" in subj or "nanosecond" in obj:
        print(subj.n3(g_rdf.namespace_manager), pred.n3(g_rdf.namespace_manager), obj.n3(g_rdf.namespace_manager))
