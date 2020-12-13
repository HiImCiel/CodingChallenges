#!/usr/bin/env python

import os
import shutil
import time

print("Start time is: " + str(time.gmtime()))

filedict = {}

print("Base folder to be copied (absolute path): ")
folder_one = input()
print("Secondary folder to omit duplicates (absolute path): ")
folder_two = input()
print("Name of new folder for base folder:  ")
new_folder1 = input()
print("Name of new folder for second folder:  ")
new_folder2 = input()


def checkfolder(folder):
    # Checks for empty folders and deletes them
    for f, s, n in os.walk(folder):
        try:
            print()
            print("Trying to delete Folder " + f + "...")
            os.rmdir(f)
            print("Deletion successful")
        except OSError:
            print()
            print("Folder " + f + " is not empty")

    for f, s, n in os.walk(folder):
        for x in n:
            bf = os.path.abspath(os.path.join(folder, x))
            if x.startswith("._"):
                print("Deleting metadata file " + x)
                os.unlink(bf)


# Checks each file against a dictionary of filesize values to see if the file is a duplicate
def duplicatecopy(filetocopy):

    for folder, sfolder, fname in os.walk(filetocopy):
        for i in fname:

            fp = os.path.abspath(os.path.join(folder, i))

            if os.path.getsize(fp) not in filedict.values():
                print("Added file: ", fp, "      ", os.path.getsize(fp), "bits")
                filedict[fp] = os.path.getsize(fp)

            elif os.path.getsize(fp) in filedict.values():
                print("this file is getting deleted: (duplicate file in first folder): " + fp)
                os.unlink(fp)


# Copies first folder & contents into new designated folder, runs function to delete duplicates based on file size
shutil.copytree(folder_one, new_folder1)
duplicatecopy(new_folder1)
checkfolder(new_folder1)

# Does same as above for folder two
shutil.copytree(folder_two, new_folder2)
duplicatecopy(new_folder2)
checkfolder(new_folder2)

# Makes new Folder for two created folders to go into
os.mkdir("D:\\FSTP")

# Moves files from folder 1 to folder FSTP & displays which files are being transferred
for foldername, subfolders, filenames in os.walk(new_folder2):
    for k in filenames:
        file_path = os.path.abspath(os.path.join(foldername, k))
        print("Moving file " + file_path + "...")

# Moves files from folder 2 to folder FSTP & displays which files are being transferred
for foldername, subfolders, filenames in os.walk(new_folder2):
    for k in filenames:
        file_path = os.path.abspath(os.path.join(foldername, k))
        print("Moving file " + file_path + "...")

shutil.move(new_folder1, "D:\\FSTP")
shutil.move(new_folder2, "D:\\FSTP")

print("End time is: " + str(time.localtime()))
