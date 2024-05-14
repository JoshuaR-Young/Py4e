fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh :
    text_split = line.split()
    for word in text_split:
        if word not in lst:
            lst.append(word)
        else :
            continue

print(sorted(lst))