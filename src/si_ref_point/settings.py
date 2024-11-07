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

