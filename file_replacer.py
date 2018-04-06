'''
A script to replace files from a source folder to a destination folder.
'''


import FileFinder
from shutil import copyfile, SameFileError
from os import sep

replacement_folder = 'replacement_folder'
replacement_files = FileFinder.get_files('replacement_folder')
all_files = FileFinder.get_all_files()
copied_files = []

for file in all_files:
    if replacement_folder in file or __file__ in file:
        continue

    for r_file in replacement_files:
        r_file_split = r_file.split(sep)
        replacement_filename = r_file_split[-1]
        if replacement_filename in file:
            try:
                copyfile(r_file, file)
                print('Successfully copied %s to %s.' % (r_file, file))
                copied_files.append(r_file)
            except OSError:
                print('Could not write %s into %s, destination directory not'
                      ' writeable.'
                      % (r_file, file))
            except SameFileError:
                print('%s is already the same as %s.' % (r_file, file))

for r_file in replacement_files:
    if r_file not in copied_files:
        print('%s was not copied.' % r_file)
