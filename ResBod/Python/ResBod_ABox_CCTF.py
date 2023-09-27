from settings import CCTF_FILES_FOLDER
from resbod_utils import MeetingsFileExtractor

mfe = MeetingsFileExtractor(
    resbod_acronym="CCTF",
    meeting_files_directory=CCTF_FILES_FOLDER,
)

mfe.create_and_save_turtle()
