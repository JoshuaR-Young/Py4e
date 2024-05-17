email = dict()
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError :
    print('File does not exist: ')
    exit()
    
for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in email:
            email[words[1]] = 1
        else: 
            email[words[1]] += 1

print(email)