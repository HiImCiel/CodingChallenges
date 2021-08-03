import os

print("File path: ")
path = input()
print("Number of episodes: ")
epi = input()
numepi = int(epi)

# change to given directory
os.chdir(path)

# defines all structures in directory
for foldername, subfolders, filenames in os.walk(path):

    # creates folders based on their episode number
    for i in range(1, numepi):
        try:
            x = "Episode " + (str(i))
            os.mkdir(x)
        except FileExistsError:
            continue
