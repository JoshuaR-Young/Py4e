
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.strip()
    print(ly.upper())
