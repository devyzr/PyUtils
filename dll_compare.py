"""
    Checks if all the dlls we have contain a corresponding .cs file,
    if not, prints the file.
"""

from FileFinder import get_all_files
from os import sep


all_files = get_all_files()

all_dlls = []
all_csharp = []

for file_path in all_files:
    separated = file_path.split(sep)
    filename = separated[-1]

    # Trim extension for easier comparing later on
    if '.cs' in filename[-3:]:
        ext_less = filename[:-3]
        all_csharp.append(ext_less)

    if '.dll' in filename[-4:]:
        ext_less = filename[:-4]
        all_dlls.append(ext_less)

all_dlls.sort()

print("Missing source code for follwing .dlls\n")
for dll in all_dlls:
    if dll not in all_csharp:
        print('%s.dll' % dll)
