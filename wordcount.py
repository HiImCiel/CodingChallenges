# Will read a file that and perform a word count, as well as a complete list of each word used

# Os needed for input
import os


# Gets absolute file path to the curent directory
print("Enter the file name to read \n(you are currently in: \n" + os.getcwd() + "\n directory):")
filename = input()
filepath = os.path.join(os.getcwd(), filename)

# TODO MAKE OPTION TO SELECT A NEW DIRECTORY

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
