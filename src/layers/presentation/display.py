from src.layers.controller.file_stack_handler import add_files_to_stack
from src.layers.controller.file_stack_handler import get_files, sort_stack
from src.layers.controller.file_stack_handler import get_files

def display_sort_stack():
    add_files_to_stack()

    for i in sort_stack():
        print(f"{i.size}kB", i.name)

def display_txt_files():
    for file_name in get_files():
        print(file_name)