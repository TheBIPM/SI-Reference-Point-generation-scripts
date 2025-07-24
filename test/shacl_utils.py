import owlrl
from pyshacl import validate
import rdflib
from rdflib import OWL


class SHACLutils:
    def load_knowledge_bases(self, knowledge_bases):
        # load them into rdflib-graph
        g_rdf = rdflib.Graph()
        for kb, kb_val in knowledge_bases.items():
            g_rdf.parse(kb_val["path"], format=kb_val["format"])

        return g_rdf

    def run_reasoner(self, g_rdf):
        # infer implicit triples by reasoning
        owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g_rdf)

        return g_rdf

    def remove_sameAs(self, g_rdf):
        # remove owl:sameAs relations, if they only cover identity
        for subj, pred, obj in g_rdf.triples((None, OWL.sameAs, None)):
            # if pred.startswith(rdflib.RDFS):
            if subj == obj:
                g_rdf.remove((subj, pred, obj))

        return g_rdf

    def show_all_triples(self, g_rdf):
        for subj, pred, obj in g_rdf.triples((None, None, None)):
            print(subj, pred, obj)

    def validate_against_constraints(self, g_data, g_shapes, verbose=False):
        r = validate(g_data, shacl_graph=g_shapes, inference="both", advanced=False)

        conforms, results_graph, results_text = r

        if verbose:
            print(results_text)

        return conforms, results_graph
