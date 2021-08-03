import os

print("File path: ")
path = input()

# change to given directory
os.chdir(path)

for foldername, subfolders, filenames in os.walk(path):
    for i in filenames:
        file_path = os.path.abspath(os.path.join(foldername, i))

        print(i)
        if i.find("ass") != -1 & i.find("enUS") == -1:
            print("removing " + file_path)
            os.unlink(file_path)

