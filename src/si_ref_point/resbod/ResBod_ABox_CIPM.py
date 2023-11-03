from si_ref_point.settings import CIPM_FILES_FOLDER
from si_ref_point.resbod.utils import MeetingsFileExtractor


def main():
    mfe = MeetingsFileExtractor(
        resbod_acronym="CIPM",
        meeting_files_directory=CIPM_FILES_FOLDER,
    )

    mfe.create_and_save_turtle()
