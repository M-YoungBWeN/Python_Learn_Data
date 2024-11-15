from ...PackageD.PrintSomething import print_data


def load_data(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        data = f.read()
        print_data(data)
