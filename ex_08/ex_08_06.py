lst = []
while True:
    num_lst = input('Enter a number: ')
#Enter numbers
    if num_lst == 'done': break
    else:
        try:
            num_lst = int(num_lst)
            num_lst = float(num_lst)
            lst.append(num_lst)
        #Error message for when a number isn't input
        except:
            print('Invalid Input')
            continue

#print Max & Min in list (lst)
print('Maximum: ', max(lst))
print('Minimum: ', min(lst))
