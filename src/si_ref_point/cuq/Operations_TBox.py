import os

from rdflib import Graph

from si_ref_point.settings import CUQ_FILES_FOLDER

def main():
    # start with empty graph
    g_ext = Graph()

    # load extended concepts into same graph
    extended_concepts_path = os.path.join(CUQ_FILES_FOLDER, "math_operations.ttl")
    g_ext.parse(extended_concepts_path, format="ttl")

    return g_ext


if __name__ == "__main__":
    main()
