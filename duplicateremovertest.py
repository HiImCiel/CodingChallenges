#!/usr/bin/env python

import os
import shutil


filedict = {}

print("Base folder to be copied (absolute path): ")
folder_one = input()

print("Secondary folder to omit duplicates (absolute path): ")
folder_two = input()

print("Name of new folder for base folder:  ")
new_folder1 = input()

print("Name of new folder for second folder:  ")
new_folder2 = input()


# TODO add check for empty folders & undesirable files (ex. starting with ._)
def checkfolder(folder):
    for f, s, n in os.walk(folder):
        try:
            os.rmdir(f)
        except OSError:
            print("OS Error")


# Checks each file against a dictionary of filesize values to see if the file is a duplicate
def duplicatecopy(filetocopy):

    for folder, sfolder, fname in os.walk(filetocopy):
        for i in fname:

            fp = os.path.abspath(os.path.join(folder, i))

            if os.path.getsize(fp) not in filedict.values():
                print("Added file: ", fp, "      ", os.path.getsize(fp), "bits")
                filedict[fp] = os.path.getsize(fp)

            elif os.path.getsize(fp) in filedict.values():
                print("this file is getting deleted: (duplicate file in first folder)" + fp)
                os.unlink(fp)


# Copies first folder & contents into new designated folder, runs function to delete duplicates based on file size
shutil.copytree(folder_one, new_folder1)
duplicatecopy(new_folder1)

# Does same as above for folder two
shutil.copytree(folder_two, new_folder2)
duplicatecopy(new_folder2)

# Moves files from folder 2 to folder 1 & displays which files are being transferred
for foldername, subfolders, filenames in os.walk(new_folder2):
    for k in filenames:
        file_path = os.path.abspath(os.path.join(foldername, k))
        print("Moving file " + file_path + "...")

shutil.move(new_folder2, new_folder1)
