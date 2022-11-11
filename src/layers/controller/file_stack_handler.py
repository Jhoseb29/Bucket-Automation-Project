from src.layers.service.file_service import FileService
from src.layers.service.stack_service import StackService
from src.layers.domain.lifo import Stack
import os
from time import sleep

stack = Stack()
file_service = FileService()
stack_service = StackService(stack)

def get_files():
    
    txt_files = file_service.get_only_txt_files()
    return txt_files

def add_files_to_stack():
    
    txt_files = file_service.get_only_txt_files()

    for filename in txt_files:
        name = filename
        size = file_service.get_size_from_filename(filename)
        path = file_service.get_standard_path()

        file = file_service.create_file(name, size, path)
        stack_service.stack.push(file)


def sort_stack():
    os.chdir(file_service.get_standard_path())
    archivos = file_service.get_only_txt_files()
    for archivo in archivos:
        sleep(1)
        if archivo.endswith(".txt"):
            if file_service.get_size_from_filename(archivo) < 1024*1024:
                if not os.path.exists("SoftFile"):
                    sleep(1)
                    os.mkdir("SoftFile")
                os.rename(archivo, "SoftFile/"+archivo)
            elif file_service.get_size_from_filename(archivo) > 1024*1024*1024:
                if not os.path.exists("MediumFile"):
                    sleep(1)
                    os.mkdir("MediumFile")
                os.rename(archivo, "MediumFile/"+archivo)
            else:
                if not os.path.exists("HardFile"):
                    sleep(1)
                    os.mkdir("HardFile")
                os.rename(archivo, "HardFile/"+archivo)

    return stack_service.stack.items()
    