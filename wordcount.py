# Will read a file that and perform a word count, as well as a complete list of each word used

# Os needed for input, shutil needed for copying
import os
import shutil


# Choose current directory file or file in another directory
print("Enter the file name to read \n(you are currently in: \n" + os.getcwd() + "\n directory):")
print("Or type 'Other Directory' to select a file in a nother directory")

# Case of file in another directory; copies file to CodingChallenges directory
od = "Other Directory"
filename = input()
if filename == od:
    print("Please input the absolute path name of the directory, including the file name")
    otherdirect = input()
    filepath = shutil.copy(otherdirect, os.getcwd())

# File is already in directory
else:
    filepath = os.path.join(os.getcwd(), filename)

# Checks validity of filepath, then puts txt contents int a dictionary
if os.path.exists(filepath):
    readfile = open(filepath)
    contents = readfile.read()
    for k in contents:
        contents.lower()
    contentlist = contents.split()
    d = {}
    for word in contentlist:
        if word not in d:
            d[word] = 0
        d[word] += 1

    # prints out word count and reverses the dictionary in word count order, then prints it
    print("wordcount in doc: " + str(len(d)))
    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))
    word_freq.sort(reverse=True)
    for i in range(len(word_freq)):
        print(word_freq[i])

else:
    print("something went wrong :(")
