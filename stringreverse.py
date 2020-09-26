# Option One
print("Enter a sentence: ")
userinput = input()
length = len(userinput)
array = []
output = ""

for i in range(length):
    output += userinput[length - 1 - i]

print(output)

# Option Two
print("Enter a sentence: ")
userinput = input()
print(userinput[::-1])

