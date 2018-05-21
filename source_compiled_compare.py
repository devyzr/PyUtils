"""
    A more generic rewrite of dll_compare.py, checks if the files with
    extensions listed in "list_of_compiled" have a coutnerpart in
    "list_of_source".
"""

from FileFinder import get_all_files
from os import sep


list_of_source = [
    'cs'
]

list_of_compiled = [
    'dll'
]


def get_all_filenames(list_of_ext):
    all_filenames = []
    for ext in list_of_ext:
        temp = []
        filepaths = get_all_files(extension=ext)
        ext = '.' + ext
        for filepath in filepaths:
            filename = filepath.split(sep)[-1]
            filename = filename[:-len(ext)]
            temp.append(filename)

        all_filenames.extend(temp)
    return all_filenames


source_filenames = get_all_filenames(list_of_source)
compiled_filenames = get_all_filenames(list_of_compiled)
compiled_filenames.sort()


print("Missing source code for follwing files:\n")
for compiled in compiled_filenames:
    if compiled not in source_filenames:
        print('%s' % compiled)
