fname = input('Enter file name: ')
fh = open(fname)
count = 0
for line in fh:
    text = line.split()
    if len(text) < 3 or text[0] != 'From':
        continue
    print(text[1])
    count += 1

print('there were',count,'line in the file with From as the first word')