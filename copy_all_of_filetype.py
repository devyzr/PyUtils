'''
A simple script to copy all files with a certain extension
to a specific destination folder.
'''

from FileFinder import get_all_files
from os import sep, mkdir
from os.path import isdir, isfile
from shutil import copyfile
from hashlib import sha512


class CopyAllFiles:

    def main(self, file_ext, dest_folder):
        self.massCopy(file_ext, dest_folder)

    def massCopy(self, file_ext, dest_folder):
        files = get_all_files('.', file_ext)

        if not isdir(dest_folder):
            mkdir(dest_folder)

        for file in files:
            # Get the filename and generate new filename
            split_f = file.split(sep)
            filename = split_f[-1]
            new_file_loc = ''.join([dest_folder, sep, filename])
            file_exists = isfile(new_file_loc)

            # Copies if file is named the same but different
            if file_exists:
                file_identical = self.checkIfSame(file, new_file_loc)
                if file_identical:
                    print("These files are identical:\n\t%s\n\t%s\n" %
                          (file, new_file_loc))
                else:
                    file_no = 1
                    f_name_part = filename[:-len(file_ext)]
                    while file_exists:
                        new_file_loc = ''.join([dest_folder, sep, f_name_part, '_',
                                                str(file_no), file_ext])
                        file_no += 1
                        file_exists = isfile(new_file_loc)

                    copied_file = copyfile(file, new_file_loc)
                    print('Copied %s\n' % copied_file)
            else:
                copied_file = copyfile(file, new_file_loc)
                print('Copied %s\n' % copied_file)

    def checkIfSame(self, file1, file2):
        digest1 = self.hashFile(file1)
        digest2 = self.hashFile(file2)

        result = digest1 == digest2
        return result

    def hashFile(self, file):
        sha = sha512()

        with open(file, 'rb') as f:
            while True:
                data = f.read(2 ** 20)
                if not data:
                    break
                sha.update(data)

        digest = sha.hexdigest()
        return digest


if __name__ == "__main__":
    dest_folder = '2_dll_dir'
    file_ext = '.dll'
    caf = CopyAllFiles()
    caf.main('.dll', dest_folder)
