""" Check the syntax and semantics of the SI graph """

import rdflib
from config import TTLPATH


def test_syntax():
    error_status = False

    ttl_file_names = TTLPATH.glob("*.ttl")

    g = None
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


def main():
    g, syntax_error = test_syntax()

    if syntax_error:
        raise ImportError("The syntax of the generated files is not ok.")

    semantic_error = test_semantics(g)
    if semantic_error:
        raise ValueError("A requirement regarding the content of the output files is not met.")

    print(syntax_error, semantic_error)


if __name__ == "__main__":
    main()
