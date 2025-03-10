import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

    @property
    def data_file_path(self) -> str:
        dirname = os.path.dirname(os.path.abspath(__file__))
        parentDir = os.path.dirname(dirname)
        file_path = os.getenv("DATA_FILE_PATH", os.path.join(parentDir,"assets", "profit-and-loss.json"))
        return file_path    

config = Config()