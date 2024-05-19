email_counts = dict()  # Dictionary to hold email counts
maximum = 0
maximum_email = ''

# Prompt user for file name
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found')
    exit()

# Process the file line by line
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        # Increment the email count
        email_counts[words[1]] = email_counts.get(words[1], 0) + 1

# Find the email with the maximum count
for address in email_counts:
    if email_counts[address] > maximum:
        maximum = email_counts[address]
        maximum_email = address

# Print the result
print(maximum_email, maximum)