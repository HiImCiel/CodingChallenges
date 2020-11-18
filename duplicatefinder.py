import os
import shutil

# Dictionary of files going into new folder
filedict = {}

print("Base folder to be copied (absolute path): ")
baseFolder = input()

print("Secondary folder to omit duplicates (absolute path): ")
compareFolder = input()

print("Name of new folder: ")
duplicateFolder = input()

# Makes new folder
os.mkdir(duplicateFolder)
os.chdir(baseFolder)

# Takes the base folder and adds it to the duplicate proof folder
print()
print("Items in base folder: ")
for foldername, subfolders, filenames in os.walk(baseFolder):
    # Prints out formatted file name & file size
    for i in filenames:
        catJam = os.path.abspath(os.path.join(foldername, i))
        print("File: ", catJam, "      ", os.path.getsize(catJam), "bits")

        if os.path.getsize(catJam) not in filedict:
            filedict[catJam] = os.path.getsize(catJam)
            shutil.copy(catJam, duplicateFolder)

# for filename in os.listdir(baseFolder):
#     if os.path.getsize((os.path.join(baseFolder, filename))) not in filedict:
#         filedict[filename] = os.path.getsize((os.path.join(baseFolder, filename)))
#         shutil.copy(filename, duplicateFolder)


# Switch directory to the new folder that is checked for duplicates
os.chdir(compareFolder)

print()
print("list of files: ")


# TODO: Add in front-end comparison by name to save computing time


for foldername, subfolders, filenames in os.walk(compareFolder):
    for i in filenames:
        catJam = os.path.abspath(os.path.join(foldername, i))
        print("File: ", catJam, "      ", os.path.getsize(catJam), "bits")
        if os.path.getsize(catJam) not in filedict:
            filedict[catJam] = os.path.getsize(catJam)
            shutil.copy(catJam, duplicateFolder)

print()
print()

print("list of files in " + compareFolder + ": ")
for x, y in filedict.items():
    print("File: ", x, "      ", y, "bits")
