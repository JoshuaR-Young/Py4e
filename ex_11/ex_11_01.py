import re

fname = input('Enter file name: ')
regex = input('Enter a regular expression: ')
count = 0

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            if re.search(regex, line):
                count += 1
except FileNotFoundError:
    print('file not found:', fname)
    exit()

print(f'{fname} had {count} lines that matched {regex}')