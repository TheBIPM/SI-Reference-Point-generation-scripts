"""
source 'settings.py'
global constants etc.
"""

from pathlib import Path


PKG_ROOT = Path(__file__).resolve().parent

SKOSURL = "http://www.w3.org/2004/02/skos/core#"
DCTURL = "http://purl.org/dc/terms#"
SIDFWBASE = "https://si-digital-framework.org"
SIRPVERSION = "1.0.0"

# Base URL for the SI Digital Framework
# from this URL, sub-URLs are defined
# - (SIDFWBASE)/SI#
# - (SIDFWBASE)/constants#
# - (SIDFWBASE)/bodies#


# Locations of input and output files

# Folder for files of cgpm + cipm resolutions
CGPM_FILES_FOLDER = PKG_ROOT / "inputs" / "rb" / "cgpm"
CIPM_FILES_FOLDER = PKG_ROOT / "inputs" / "rb" / "cipm"
CCTF_FILES_FOLDER = PKG_ROOT / "inputs" / "rb" / "cctf"

# Folder for YAML- and TTL-files produced manually
SI_FILES_FOLDER = PKG_ROOT / "inputs" / "si"

# Default Folder for output files
#   Deprecated : per default, the output will be placed in the directory
#   from which the script is launched
# TTL_FILES_FOLDER = TTLPATH
# JSONLD_FILES_FOLDER = JLDPATH

GITHUB_BASE_PATH = "https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/"

# SI_BROCHURE_PID="SI_Brochure_ed3_V4_01" # will be transformed into a PID '(SIDFWBASE)/SI/entities/(SI_BROCHURE_PID)'

# Licences
CC_LICENCE = "https://creativecommons.org/licenses/by/4.0/"
CC_LICENCE_TEXT_EN = """The SI Reference Point Ontology developed by the BIPM is licensed under CC-BY-4.0.
For further information visit https://www.bipm.org/en/copyright."""
CC_LICENCE_TEXT_FR = """L'ontologie SI Reference Point developpée par le BIPM est sous licence CC-BY-4.0.
Pour plus d'informations, consultez https://www.bipm.org/fr/copyright."""
