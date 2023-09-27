from settings import CGPM_FILES_FOLDER
from resbod_utils import MeetingsFileExtractor

mfe = MeetingsFileExtractor(
    resbod_acronym="CGPM",
    meeting_files_directory=CGPM_FILES_FOLDER,
)

mfe.create_and_save_turtle()
