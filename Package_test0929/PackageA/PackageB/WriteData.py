from ..PackageD.PrintSomething import print_data
from .PackageC import load_data

def write_data(file_path, w_str):
    with open(file_path, "a", encoding='utf-8') as f:
        f.write("\n"+w_str)

    load_data(file_path)
