print("Enter a sentence: ")
input = input()
length = len(input)
array = []
output = ""

for i in range(length):
    output += input[length - 1 - i]

print(output)


