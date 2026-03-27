""" definition of configuration variables used in the repository files """
from pathlib import Path

# Get the absolute path of the current file's parent directory (the project root)
PROJECT_ROOT = Path(__file__).resolve().parent

# create reuseable paths
TTLPATH = PROJECT_ROOT / 'outputs' / 'ttl'
JLDPATH = PROJECT_ROOT / 'outputs' / 'jsonld'
DOCPATH = PROJECT_ROOT / 'docs'
VOCPATH = PROJECT_ROOT / 'docs' / 'vocabulary'
