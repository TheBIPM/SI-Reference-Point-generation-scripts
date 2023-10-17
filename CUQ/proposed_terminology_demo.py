import owlrl
import rdflib
from rdflib import OWL, RDF, RDFS

# where knowledge bases are stored
knowledge_bases = {
    "si_derived_additions": {"path": "CUQ/proposed_terminology_for_derived_UQD.ttl", "format": "ttl"},
    "si_base": {"path": "Testing/API/si.ttl", "format": "ttl"},
    "units": {"path": "Testing/API/units.ttl", "format": "ttl"},
    "quantities": {"path": "Testing/API/quantities.ttl", "format": "ttl"},
} 

# load them into rdflib-graph
g_rdf = rdflib.Graph()
for kb, kb_val in knowledge_bases.items():
    g_rdf.parse(kb_val["path"], format=kb_val["format"])

# infer implicit triples by reasoning
owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g_rdf)

# remove owl:sameAs relations, if they only cover identity
for subj, pred, obj in g_rdf.triples((None, RDF.type, None)):

    #if "hasFactor" in pred:
    #    print(subj.n3(g_rdf.namespace_manager), pred.n3(g_rdf.namespace_manager), obj.n3(g_rdf.namespace_manager))

    #if "custom_newton" in subj or "custom_newton" in obj:
    #    print(subj.n3(g_rdf.namespace_manager), pred.n3(g_rdf.namespace_manager), obj.n3(g_rdf.namespace_manager))


    if "second_custom" in subj or "second_custom" in obj:
        print(subj.n3(g_rdf.namespace_manager), pred.n3(g_rdf.namespace_manager), obj.n3(g_rdf.namespace_manager))
