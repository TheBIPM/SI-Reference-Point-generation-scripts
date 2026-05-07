""" Check the syntax and semantics of the SI graph """

import rdflib
from si_ref_point import main as sirpmain

def verify_syntax(ttlpath):
    error_status = False

    ttl_file_names = ttlpath.glob("*.ttl")

    g = None
    try:
        g = rdflib.Graph()

        for file_name in ttl_file_names:
            g.parse(file_name)

    except SyntaxError:
        error_status = True

    return g, error_status


def verify_semantics(g):
    error_status = False

    # some not very elaborate tests
    if len(list(g.triples((None, None, None)))) < 1:
        error_status = True

    return error_status


# ttlpath is a pytest fixture, defined in conftest.py
def test_main(TTLpath):
    g, syntax_error = verify_syntax(TTLpath)

    if syntax_error:
        raise ImportError("The syntax of the generated files is not ok.")
    assert not syntax_error

    semantic_error = verify_semantics(g)
    if semantic_error:
        raise ValueError("A requirement regarding the content of the output files is not met.")
    assert not semantic_error

if __name__ == "__main__":
    test_main()
