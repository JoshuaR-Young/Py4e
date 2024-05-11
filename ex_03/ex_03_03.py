try:
    score = float(input('Enter score: '))
    if score < 0 or score > 1:
        raise ValueError
except:
    print('Bad score')
    quit()

grade = 'F'

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'

print(grade)