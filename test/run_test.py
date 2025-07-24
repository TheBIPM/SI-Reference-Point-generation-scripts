import rdflib
from pathlib import Path

from shacl_utils import SHACLutils

common_knowledge_bases = {
    "si": {"path": "TTL/si.ttl", "format": "ttl"},
    "prefixes": {"path": "TTL/prefixes.ttl", "format": "ttl"},
    "units": {"path": "TTL/units.ttl", "format": "ttl"},
}

constraint_shapes = {
    "test": {"path": "test/test_constraints.ttl", "format": "ttl"},
}


def test_syntax():
    error_status = False

    this_dir = Path(__file__).parent
    ttl_file_names = (this_dir.parent / "TTL").glob("*.ttl")

    try:
        g = rdflib.Graph()

        for file_name in ttl_file_names:
            g.parse(file_name)

    except SyntaxError:
        error_status = True

    return g, error_status


def test_semantics(g):
    error_status = False

    # some not very elaborate test
    if len(list(g.triples((None, None, None)))) < 1:
        error_status = True

    return error_status


def test_valid_individuals():
    uh = SHACLutils()

    invalid_individuals = {
        "ex": {"path": "test/valid_individuals.ttl", "format": "ttl"},
    }

    # SHACL validation
    data = invalid_individuals
    onto = common_knowledge_bases
    shapes = constraint_shapes

    data_graph = uh.load_knowledge_bases(data | onto)
    shapes_graph = uh.load_knowledge_bases(shapes)

    conforms, results_graph = uh.validate_against_constraints(data_graph, shapes_graph)

    error_status = not conforms  # if data conforms to shape, this means no error
    return error_status


def test_invalid_individuals():
    uh = SHACLutils()

    invalid_individuals = {
        "ex": {"path": "test/invalid_individuals.ttl", "format": "ttl"},
    }

    # SHACL validation
    data = invalid_individuals
    onto = common_knowledge_bases
    shapes = constraint_shapes

    data_graph = uh.load_knowledge_bases(data | onto)
    shapes_graph = uh.load_knowledge_bases(shapes)

    conforms, results_graph = uh.validate_against_constraints(data_graph, shapes_graph)

    for s, p, o in results_graph.triples((None, rdflib.SH["result"], None)):
        focusNode = results_graph.value(o, rdflib.SH["focusNode"])
        message = results_graph.value(o, rdflib.SH["resultMessage"])

        print("Focus node:     ", focusNode)
        print("Result message: ", message)
        print("")

    error_status = conforms  # if data conforms to shape, this means error
    return error_status


def main():
    g, syntax_error = test_syntax()
    if syntax_error:
        raise ImportError("The syntax of the generated files is not ok.")

    semantic_error = test_semantics(g)
    if semantic_error:
        raise ValueError(
            "A requirement regarding the content of the output files is not met."
        )

    shacl_error_valid_ind = test_valid_individuals()

    shacl_error_invalid_ind = test_invalid_individuals()

    print(syntax_error, semantic_error, shacl_error_valid_ind, shacl_error_invalid_ind)


if __name__ == "__main__":
    main()
