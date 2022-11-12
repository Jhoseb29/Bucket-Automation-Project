import os
from os import listdir
from src.layers.domain.file import File


# * Class meant to manipulate Files
class FileService:

    def __init__(self) -> None:
        self.BASE_PATH = os.getenv("BASE_PATH")
    
    def get_only_txt_files(self):
        txt_files = [
            file for file in listdir(self.BASE_PATH) 
            if os.path.isfile(os.path.join(self.BASE_PATH, file)) 
            and ".txt" in file]
        return txt_files
    
    def get_size_from_filename(self, filename):
        return os.path.getsize(f"{self.BASE_PATH}/{filename}")
    
    def get_standard_path(self):
        return self.BASE_PATH


    def create_file(self, name, size, path) -> File:
        '''Object creation explicit style'''
        file = File()
        file.name=name
        file.size=size
        file.path=path

        return file
