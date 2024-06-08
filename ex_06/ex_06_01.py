#Get input from user
inp = input('Enter a word: ')

index = len(inp) - 1

#Use while loop to traverse the string backwards
while index >= 0:
    print(inp[index])
    index -= 1