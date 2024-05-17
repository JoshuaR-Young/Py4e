day_of_week = dict()
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('Invalid input')
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    else:
        if words[2] not in day_of_week:
            day_of_week[words[2]] = 1
        else:
            day_of_week[words[2]] +=1

print(day_of_week)