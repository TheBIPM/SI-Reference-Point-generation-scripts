import os
import pathlib
package_dir = pathlib.Path(__file__).parent.resolve()

SKOSURL = "http://www.w3.org/2004/02/skos/core#"
DCTURL = "http://purl.org/dc/terms#"
SIDFWBASE = "https://si-digital-framework.org"      # Base URL for the SI Digital Framework
                                                    # from this URL, sub-URLs are defined
                                                    # - (SIDFWBASE)/SI#
                                                    # - (SIDFWBASE)/constants#
                                                    # - (SIDFWBASE)/bodies#
                                                    


# Locations of input and output files

# Folder for files of cgpm + cipm resolutions
CGPM_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cgpm")
CIPM_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cipm")
CCTF_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cctf")

# Folder for XLS-files for constants, units, quantities
CUQ_FILES_FOLDER = os.path.join(package_dir, "cuq_data")

# Default Folder for output files
TTL_FILES_FOLDER = os.path.join(package_dir, "..", "..","TTL")
JSONLD_FILES_FOLDER = os.path.join(package_dir,"..","..","JSON-LD")

# Release date
RELEASE_DATE = "2024-12-17"

# Version of the generating software
# (The version of the Python code generating the TTL files.
#  not to be confused witht the version of the knowledge graph.
#  The code can be changed without necessarily a change of the knowledge graph)
GENERATING_SW_VERSION = "0.5.0"

# Licences
CC_LICENCE = "http://creativecommons.org/licenses/by/4.0/"
CC_LICENCE_TEXT_EN = """The SI Reference Point Ontology by developer BIPMs is
licensed under CC BY 4.0. You are free to share (copy and redistribute
the material in any medium or format) and adapt (remix, transform, and
build upon the material) for any purpose, even commercially, for any
purpose, even commercially. The licensor cannot revoke these freedoms as
long as you follow the license terms. You must give appropriate credit
(by using the original ontology IRI for the whole ontology and original
term IRIs for individual terms), provide a link to the license, and
indicate if any changes were made. You may do so in any reasonable
manner, but not in any way that suggests the licensor endorses you or
your use."""
