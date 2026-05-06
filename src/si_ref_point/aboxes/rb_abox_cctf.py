"""
CCTF ABox
"""
from si_ref_point.settings import CCTF_FILES_FOLDER
from si_ref_point.aboxes.rb_utils import MeetingsFileExtractor


def main():
    mfe = MeetingsFileExtractor(
        resbod_acronym="CCTF",
        meeting_files_directory=CCTF_FILES_FOLDER,
    )

    return mfe.create_and_return_graph()
