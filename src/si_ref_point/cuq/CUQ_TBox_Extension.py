import os
from rdflib import Graph

from si_ref_point.settings import CUQ_FILES_FOLDER

def main():
    g = Graph()
    for ttl_file in ['CUQ_core_concepts.ttl',
                     'CUQ_extended_concepts.ttl']:
        g.parse(os.path.join(CUQ_FILES_FOLDER, ttl_file), format="ttl")
    return g


if __name__ == "__main__":
    main()
