'''
This is meant to get all the files in a directory tree and copy them into a
source tree where they can be examined more thoroughly. This won't watch for
duplicate files without an extension, so watch out for that.
'''

import FileFinder
from os import mkdir, sep
from shutil import copy2
from os.path import exists

all_files = FileFinder.get_all_files()
dir_name = "./Source Files"

mkdir(dir_name)

not_copied = []
copy_no = 0
for f in all_files:
    fname = f.split(sep)[-1]
    new_fpath = dir_name + sep + fname
    file_exists = exists(new_fpath)
    file_counter = 1
    # check if filename exists, if it does, make a new filename
    while file_exists:
        fileno = "_" + str(file_counter) + "."
        # Only split the right-most dot, extensions only.
        fname2 = fileno.join(fname.rsplit(".", 1))
        new_fpath = dir_name + sep + fname2
        file_counter += 1
        file_exists = exists(new_fpath)

    copy2(f, new_fpath)
    copy_no += 1
    print("copied %s from %s" % (new_fpath, f))

print("\nCopied %i files out of %i" % (copy_no, len(all_files)))
