import os

print("File path: ")
path = input()
print("Episode range (separated by comma): ")
epi = input()

epi1 = int(epi.split(",")[0])
epi2 = int(epi.split(",")[1])

# change to given directory
os.chdir(path)

# defines all structures in directory
for foldername, subfolders, filenames in os.walk(path):

    # creates folders based on their episode number
    for i in range(epi1, epi2 + 1):
        try:
            x = "Episode " + (str(i))
            os.mkdir(x)
        except FileExistsError:
            continue
