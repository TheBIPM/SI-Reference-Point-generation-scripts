"""
source 'settings.py'
global constants etc.
"""

from config import PROJECT_ROOT


SKOSURL = "http://www.w3.org/2004/02/skos/core#"
DCTURL = "http://purl.org/dc/terms#"
SIDFWBASE = "https://si-digital-framework.org"      # Base URL for the SI Digital Framework
                                                    # from this URL, sub-URLs are defined
                                                    # - (SIDFWBASE)/SI#
                                                    # - (SIDFWBASE)/constants#
                                                    # - (SIDFWBASE)/bodies#


# Locations of input and output files

# Folder for files of cgpm + cipm resolutions
CGPM_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "resbod_data" / "cgpm"
CIPM_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "resbod_data" / "cipm"
CCTF_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "resbod_data" / "cctf"

# Folder for YAML- and TTL-files produced manually
CUQ_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "cuq_data"

# Default Folder for output files
#   per default, the output will be placed in the directory
#   from which the script is launched 
TTL_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "TTL"
JSONLD_FILES_FOLDER = PROJECT_ROOT / "src" / "si_ref_point" / "JSON-LD"

GITHUB_BASE_PATH = "https://github.com/TheBIPM/SI-Reference-Point-2023/"



#SI_BROCHURE_PID="SI_Brochure_ed3_V3_01" # will be transformed into a PID '(SIDFWBASE)/SI/entities/(SI_BROCHURE_PID)'

# Licences
CC_LICENCE = "https://creativecommons.org/licenses/by/3.0/igo/"
CC_LICENCE_TEXT_EN = """The SI Reference Point Ontology developed by the BIPM is
licensed under CC-BY-3.0-IGO. You are free to share (copy and redistribute
the material in any medium or format) and adapt (remix, transform, and
build upon the material) for any purpose, even commercially, for any
purpose, even commercially. The licensor cannot revoke these freedoms as
long as you follow the license terms. You must give appropriate credit
(by using the original ontology IRI for the whole ontology and original
term IRIs for individual terms), provide a link to the license, and
indicate if any changes were made. You may do so in any reasonable
manner, but not in any way that suggests the licensor endorses you or
your use."""
CC_LICENCE_TEXT_FR = """L'ontologie SI Reference Point developpée par le BIPM est sous
licence CC-BY-3.0-IGO. Vous êtes autorisés à partager (copier, distribuer et communiquer
le matériel par tous moyens et sous tous formats) et adapter (remixer, transformer
et créer à partir du matériel) pour toute utilisation, y compris commerciale.
L'Offrant ne peut retirer les autorisations concédées par la licence tant que
vous appliquez les termes de cette licence. Vous devez créditer l'oeuvre 
(en utilisant l'IRI de l'ontologie originale pour l'ontologie entière 
et les IRIs originaux des termes individuels), intégrer un lien vers la licence 
et indiquer si des modifications ont été effectuées à l'oeuvre.
Vous devez indiquer ces informations par tous les moyens raisonnables, 
sans toutefois suggérer que l'offrant vous soutient ou soutient 
la façon dont vous avez utilisé son Oeuvre."""
