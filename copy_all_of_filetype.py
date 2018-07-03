'''
A simple script to copy all files with a certain extension
to a specific destination folder.
'''

from FileFinder import get_all_files
from os import sep, mkdir
from os.path import isdir, isfile
from shutil import copyfile


class CopyAllFiles:

    def massCopy(self, file_ext, dest_folder):
        files = get_all_files('.', file_ext)

        if not isdir(dest_folder):
            mkdir(dest_folder)

        for file in files:
            # Get the filename
            split_f = file.split(sep)
            filename = split_f[-1]
            new_file_loc = ''.join([dest_folder, sep, filename])
            file_exists = isfile(new_file_loc)
            if file_exists:
                file_no = 1
                while file_exists:
                    new_file_loc = ''.join([dest_folder, sep, filename, '_',
                                            str(file_no)])
                    file_no += 1
                    file_exists = isfile(new_file_loc)

            copied_file = copyfile(file, new_file_loc)
            print('Copied %s' % copied_file)


if __name__ == "__main__":
    file_ext = ''
    dest_folder = 'copied_files'
    CopyAllFiles.massCopy(file_ext, dest_folder)
