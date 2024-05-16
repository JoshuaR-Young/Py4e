count = 0
wordstxt = dict()
fname = open('words.txt')
for line in fname:
    words = line.split()
    for word in words:
        count += 1
        if word in wordstxt:
            continue
        wordstxt[word] = count

if 'computers' in wordstxt:
    print('True')
else:
    print('False')
