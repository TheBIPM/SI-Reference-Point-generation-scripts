""" definition of configuration variables used in the repository files """
from pathlib import Path

# Get the absolute path of the current file's parent directory (the project root)
PROJECT_ROOT = Path(__file__).resolve().parent

# create reuseable paths
TTLPATH = PROJECT_ROOT / 'src' / 'si_ref_point' / 'TTL'
JLDPATH = PROJECT_ROOT / 'src' / 'si_ref_point' / 'JSON-LD'
