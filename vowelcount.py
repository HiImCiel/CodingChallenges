# counts all the vowels in a sentence
print("Enter a sentence: ")
sentence = input()
voweldictionary = {"a": 0, "e": 0,  "i": 0, "o": 0, "u": 0}

for i in range(len(sentence)):
    if sentence[i] in voweldictionary.keys():
        voweldictionary[sentence[i]] += 1


print(voweldictionary)

