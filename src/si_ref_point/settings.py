import os
import pathlib
package_dir = pathlib.Path(__file__).parent.resolve()

SIURL = "https://si-digital-framework.org/"
SKOSURL = "http://www.w3.org/2004/02/skos/core#"
DCTURL = "http://purl.org/dc/terms#"

# Base URL of the API
BASE_URL = "http://localhost:8000/"

# Locations of input and output files

# Folder for files of cgpm + cipm resolutions
CGPM_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cgpm")
CIPM_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cipm")
CCTF_FILES_FOLDER = os.path.join(package_dir, "resbod_data", "cctf")

# Folder for XLS-files for constants, units, quantities
CUQ_FILES_FOLDER = os.path.join(package_dir, "cuq_data")

# Folder for API
APIPATH = "./API/"
