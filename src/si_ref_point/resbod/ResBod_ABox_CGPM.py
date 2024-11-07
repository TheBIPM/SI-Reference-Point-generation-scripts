"""
CGPM ABox
"""
from si_ref_point.settings import CGPM_FILES_FOLDER
from si_ref_point.resbod.utils import MeetingsFileExtractor


def main():
    mfe = MeetingsFileExtractor(
        resbod_acronym="CGPM",
        meeting_files_directory=CGPM_FILES_FOLDER,
    )

    return mfe.create_and_return_graph()
