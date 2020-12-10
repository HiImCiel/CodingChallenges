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

shutil.copytree(folder_one, new_folder1)

for foldername, subfolders, filenames in os.walk(new_folder1):
    for i in filenames:

        file_path = os.path.abspath(os.path.join(foldername, i))

        if os.path.getsize(file_path) not in filedict.values():
            print("Added file: ", file_path, "      ", os.path.getsize(file_path), "bits")
            filedict[file_path] = os.path.getsize(file_path)

        elif os.path.getsize(file_path) in filedict.values():
            print("this file is getting deleted: (duplicate file in first folder)" + file_path)
            os.unlink(file_path)

shutil.copytree(folder_two, new_folder2)

for foldername, subfolders, filenames in os.walk(new_folder2):
    for i in filenames:

        file_path = os.path.abspath(os.path.join(foldername, i))

        if os.path.getsize(file_path) not in filedict.values():
            print("Added file: ", file_path, "      ", os.path.getsize(file_path), "bits")
            filedict[file_path] = os.path.getsize(file_path)

        elif os.path.getsize(file_path) in filedict.values():
            print("this file is getting deleted: (duplicate file in second folder)" + file_path)
            os.unlink(file_path)

for foldername, subfolders, filenames in os.walk(new_folder2):
    for i in filenames:
        file_path = os.path.abspath(os.path.join(foldername, i))
        print("Moving file " + file_path + "...")

shutil.move(new_folder2, new_folder1)

