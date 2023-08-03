""" file that contains variables to configure paths etc. across the project """
from localsettings import *

# project base


SIURL = "http://si-digital-framework.org/"
SKOSURL = "http://www.w3.org/2004/02/skos/core#"
DCTURL = "http://purl.org/dc/terms#"

#Base URL of the API
BASE_URL = "http://localhost:8000/"

### Locations of input and output files
# 

# project base
PROJECTBASE = LOCALBASE + "Semantic-SI/"

# Folder for files of cgpm resolutions
CGPM_FILES_FOLDER = PROJECTBASE + "ResBod/_docs/cgpm/"

# Folder for XLS-files for constants, units, quantities 
XLS_FILES_FOLDER = PROJECTBASE + "CUQ/_docs/"

# Folder for API (this is also the location of the output TTL files)
APIPATH = PROJECTBASE + "Testing/API/"
