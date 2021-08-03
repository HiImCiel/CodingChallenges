import os

print("File path: ")
path = input()

# change to given directory
os.chdir(path)

# defines all structures in directory
for foldername, subfolders, filenames in os.walk(path):

    # creates folders based on their episode number
    for i in range(1, 15):
        try:
            x = "Episode " + (str(i))
            os.mkdir(x)
        except FileExistsError:
            continue
