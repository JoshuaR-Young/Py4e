fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        fhand = open(fname)
        count = 0
        for line in fhand:
            if line.startswith('Subject:'):
                count += 1
        fhand.close()
        print('There were', count, 'subject lines in', fname)
    except FileNotFoundError:
        print(f'File not found: {fname}')
