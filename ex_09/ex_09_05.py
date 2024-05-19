from collections import defaultdict

#defaultdict initializes counts to 0 by default
email_records = defaultdict(int)

fname = input('Enter file name: ')
try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            #Check if the line starts with 'From' and has enough words
            words = line.split()
            if len(words) < 3 or words[0] != 'From':
                continue
            #Extract the email address and the domain
            email = words[1]
            domain = email.split('@')[1]
            # Increment the domain count
            email_records[domain] += 1
                
except FileNotFoundError:
    print('file not found', (fname))
    exit()

print(email_records)
