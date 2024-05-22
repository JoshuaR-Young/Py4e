from collections import defaultdict
fname = input('Enter file name: ')
hour_count = defaultdict(int)

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            words = line.split()
            if len(words) < 6 or words[0] != 'From':
                continue

            time = words[5]
            hours = time.split(':')[0]
            hour_count[hours] += 1
except FileNotFoundError:
    print('File does not exist')
    exit()

for hours in sorted(hour_count):
    print(hours, hour_count[hours])