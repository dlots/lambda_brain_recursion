import os


def recursive_search_all_files(path, files):
    for basename in os.listdir(path):
        next_path = os.path.join(path, basename)
        if os.path.isfile(next_path):
            files.append(next_path)
        elif os.path.isdir(next_path):
            recursive_search_all_files(next_path, files)


def search_all_files(path):
    result = []
    recursive_search_all_files(path, result)
    return result
