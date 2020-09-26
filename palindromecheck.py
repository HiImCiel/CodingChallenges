# checks to see if a sentence is a palindrome
print("Enter a sentence: ")
sentence = input()
length = len(sentence)
halfway = int(length/2)

# palindromes that have even number of characters
if length % 2 == 0:
    firsthalf = sentence[0:halfway]
    secondhalf = sentence[halfway:length]
    secondhalfback = secondhalf[::-1]
    x = 0
    for i in range(len(firsthalf)):
        if firsthalf[i] == secondhalfback[i]:
            x = 0
        else:
            x += 1

    if x == 0:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")


# palindromes that have odd numbers of characters
if length % 2 == 1:
    firsthalf = sentence[0:halfway]
    secondhalf = sentence[halfway + 1:length]
    secondhalfback = secondhalf[::-1]
    x = 0
    for i in range(len(firsthalf)):
        if firsthalf[i] == secondhalfback[i]:
             x = 0
        else:
             x += 1

    if x == 0:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
