'''
A simple script to copy all files with a certain extension
to a specific destination folder.
'''

from FileFinder import get_all_files
from os import sep, mkdir
from os.path import isdir, isfile
from shutil import copyfile

files = get_all_files()
dest_folder = 'copied_files'
file_ext = ''

if not isdir(dest_folder):
    mkdir(dest_folder)

for file in files:
    split_f = file.split(sep)
    filename = split_f[-1]
    if file_ext in filename:
        split_filename = filename.split('.')
        filename = '.'.join(split_filename[:-2])
        new_file_loc = ''.join([dest_folder, sep, filename, file_ext])
        file_exists = isfile(new_file_loc)
        if file_exists:
            file_no = 1
            while file_exists:
                new_file_loc = ''.join([dest_folder, sep, filename, '_',
                                        str(file_no), file_ext])
                file_no += 1
                file_exists = isfile(new_file_loc)

        print('Copying %s' % new_file_loc)
        copied_file = copyfile(file, new_file_loc)