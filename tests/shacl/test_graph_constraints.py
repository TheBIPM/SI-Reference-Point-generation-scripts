"""
demonstration of SHACL shapes to detect possible issues with the RDF that is being generated
- EndValidityDate after StartValidityDate
- detect (in)valid PrefixedUnits
"""

from pathlib import Path

import owlrl
import rdflib
from pyshacl import validate
from rdflib import OWL

parent_dir = Path(__file__).parent


class SHACLutils:
    def load_knowledge_bases(self, knowledge_bases):
        # load them into rdflib-graph
        g_rdf = rdflib.Graph()
        for kb, kb_val in knowledge_bases.items():
            g_rdf.parse(kb_val, format="ttl")

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


def test_siunits_definitions(TTLpath):
    df = TTLpath / "units.ttl"
    dff = "turtle"
    assert df.exists()

    sf = parent_dir / "unit_definition_shacl.ttl"
    sff = "turtle"
    assert sf.exists()

    conforms, v_graph, v_text = validate(
        str(df),
        shacl_graph=str(sf),
        data_graph_format=dff,
        shacl_graph_format=sff,
        inference="rdfs",
        debug=False,
        serialize_report_graph=True,
    )
    print(v_text)
    assert conforms


def test_resbod_property_types(TTLpath):

    uh = SHACLutils()

    common_knowledge_bases = {
        "rb": TTLpath / "bodies.ttl",
        "cipm": TTLpath / "cipm.ttl",
        "cgpm": TTLpath / "cgpm.ttl",
        "cctf": TTLpath / "cctf.ttl",
    }
    constraint_shapes = {"test": parent_dir / "resbod_shacl.ttl"}

    # SHACL validation
    data_graph = uh.load_knowledge_bases(common_knowledge_bases)
    shapes_graph = uh.load_knowledge_bases(constraint_shapes)

    conforms, results_graph = uh.validate_against_constraints(
        data_graph, shapes_graph, verbose=True
    )

    assert conforms


def test_valid_prefixedunit_individuals(TTLpath):

    uh = SHACLutils()

    common_knowledge_bases = {
        "si": TTLpath / "si.ttl",
        "prefixes": TTLpath / "prefixes.ttl",
        "units": TTLpath / "units.ttl",
    }
    constraint_shapes = {"test": parent_dir / "prefixedunits_shacl.ttl"}
    valid_individuals = {"ex": parent_dir / "prefixedunits_valid_individuals.ttl"}

    # SHACL validation
    data_graph = uh.load_knowledge_bases(valid_individuals | common_knowledge_bases)
    shapes_graph = uh.load_knowledge_bases(constraint_shapes)

    conforms, results_graph = uh.validate_against_constraints(data_graph, shapes_graph)

    assert conforms


def test_invalid_prefixedunit_individuals(TTLpath):
    uh = SHACLutils()

    common_knowledge_bases = {
        "si": TTLpath / "si.ttl",
        "prefixes": TTLpath / "prefixes.ttl",
        "units": TTLpath / "units.ttl",
    }
    constraint_shapes = {"test": parent_dir / "prefixedunits_shacl.ttl"}
    invalid_individuals = {"ex": parent_dir / "prefixedunits_invalid_individuals.ttl"}

    # SHACL validation
    data_graph = uh.load_knowledge_bases(invalid_individuals | common_knowledge_bases)
    shapes_graph = uh.load_knowledge_bases(constraint_shapes)

    conforms, results_graph = uh.validate_against_constraints(data_graph, shapes_graph)

    for s, p, o in results_graph.triples((None, rdflib.SH["result"], None)):
        focusNode = results_graph.value(o, rdflib.SH["focusNode"])
        message = results_graph.value(o, rdflib.SH["resultMessage"])

        print("Focus node:     ", focusNode)
        print("Result message: ", message)
        print("")

    # if data conforms to shape, this means error (expectation is an INVALID individual)
    assert not conforms


if __name__ == "__main__":
    test_siunits_definitions(Path("tests/TTL"))
    test_resbod_property_types(Path("tests/TTL"))
    test_valid_prefixedunit_individuals(Path("tests/TTL"))
    test_invalid_prefixedunit_individuals(Path("tests/TTL"))
