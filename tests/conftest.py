import pytest
from pathlib import Path
from si_ref_point import main as sirpmain

@pytest.fixture(scope="session")
def TTLpath():
    testrootdir = Path(__file__).parent
    ttlpath = testrootdir / 'TTL'
    sirpmain.non_interactive(ttlpath)
    return ttlpath
