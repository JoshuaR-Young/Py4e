count = 0
wordstxt = dict()
fname = open('words.txt')
for line in fname:
    words = line.split()
    for word in words:
        wordstxt[word] = wordstxt.get(word,0) + 1

if 'computers' in wordstxt:
    print('True')
else:
    print('False')
