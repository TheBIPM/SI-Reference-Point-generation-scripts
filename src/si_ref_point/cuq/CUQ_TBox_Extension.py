import os

from si_ref_point.cuq.CUQ_TBox import SiElements
from si_ref_point.settings import APIPATH, CUQ_FILES_FOLDER

def main():
    # load ontology as graph from the generating script
    si_base_onto = SiElements()
    g_ext = si_base_onto.g

    # load extended concepts into same graph
    extended_concepts_path = os.path.join(CUQ_FILES_FOLDER, "CUQ_extended_concepts.ttl")
    g_ext.parse(extended_concepts_path, format="ttl")

    return g_ext


if __name__ == "__main__":
    main()
