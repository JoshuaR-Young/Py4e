Minimum = None
Maximum = None
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    if Minimum is None or fval < Minimum :
        Minimum = fval
    if Maximum is None or fval > Maximum :
        Maximum = fval

#print ('Min, Max')
print('Minimum:',Minimum,'Maximum:',Maximum)