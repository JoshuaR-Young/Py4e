from collections import defaultdict
fname = input('Enter file: ')
email_counts = defaultdict(int)

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            words = line.split()
            if len(words) < 3 or words[0] != 'From':
                continue
            
            email = words[1]
            email_counts[email] += 1 

except FileNotFoundError:
    print('File not found')
    exit()

#Create a list of (Count, Email) tuples from the dictionary
count_email_list = [(count, email) for email, count in email_counts.items()]

#Sort the list from Greatest to Least
count_email_list.sort(reverse=True)

#Print from Greatest to Least
if count_email_list:
    most_commits = count_email_list[0]
    print(most_commits[1], most_commits[0])
else:
    print('No "From" lines fount int the file')
