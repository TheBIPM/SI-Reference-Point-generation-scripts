from settings import CIPM_FILES_FOLDER
from resbod_utils import MeetingsFileExtractor

mfe = MeetingsFileExtractor(
    resbod_acronym="CIPM",
    meeting_files_directory=CIPM_FILES_FOLDER,
)

mfe.create_and_save_turtle()
