import re
fname = input('Enter file name: ')
#initialize a list to store the extracted numbers
numbers = []

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            line = line.rstrip()
            # Use findall to extract the numbers from lines matching the pattern
            matches = re.findall('^New Revision: ([0-9.]+)', line)
            if matches:
                #Convert matched string to an integer and add to the list
                number = int(matches[0])
                numbers.append(number)
except FileNotFoundError:
    print('File not found', fname)
    exit()

#compute the average of the numbers
if numbers:
    average = sum(numbers) / len(numbers)
    print(int(average))
else:
    print('No matching lines found')