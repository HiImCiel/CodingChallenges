import os
import shutil

filedict = {}

keepFolder = 'D:\\testDeletionKeep'
deleteFolder = 'D:\\testDeletionDelete'
nodupFolder = 'D:\\noduplicates'

os.mkdir('D:\\noduplicates')

os.chdir(keepFolder)

for foldername, subfolders, filenames in os.walk(keepFolder):
    for filename in os.listdir(keepFolder):
        if os.path.getsize((os.path.join(keepFolder, filename))) not in filedict:
            filedict[filename] = os.path.getsize((os.path.join(keepFolder, filename)))
            shutil.copy(filename, nodupFolder)

for x, y in filedict.items():
    print(x, y)

os.chdir(deleteFolder)

for foldername, subfolders, filenames in os.walk(deleteFolder):
    for filename in os.listdir(deleteFolder):
        if os.path.getsize((os.path.join(deleteFolder, filename))) not in filedict:
            filedict[filename] = os.path.getsize((os.path.join(deleteFolder, filename)))
            shutil.copy(filename, nodupFolder)

print()
print()

for x, y in filedict.items():
    print(x, y)
