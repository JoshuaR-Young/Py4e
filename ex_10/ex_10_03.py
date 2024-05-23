from collections import defaultdict
import string
fname = input('Enter file name: ')
letter_counts = defaultdict(int)

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            for char in line:
                char = char.lower()
                if char in string.ascii_lowercase:
                    letter_counts[char] += 1
except FileNotFoundError:
    print('File not found:', fname)
    exit()

count_letter_list = [(count, letter) for letter, count in letter_counts.items()]
count_letter_list.sort(reverse=True, key=lambda x: x[0])

for count, letter in count_letter_list:
    print(letter, count)