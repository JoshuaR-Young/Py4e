fhand = open('mbox-short.txt')

# Initialize count
count = 0

# Loop through each line in the file
for line in fhand:
    # Split the line into words
    words = line.split()
    
    # Combine the guard conditions into a single if statement
    if len(words) == 0 or words[0] != 'From':
        continue

    # Print the third word
    print(words[2])

# Close the file
fhand.close()