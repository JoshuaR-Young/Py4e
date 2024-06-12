def chop(lst):
    #Remove the first and last elements of the list, Modify the list in place and retun None.
    if len(lst) > 1:
        del lst[0]
        del lst[-1]
    elif len(lst) == 1:
        lst.clear()
    return None

def middle(lst):
    return lst[1:-1]

test_list = [1, 2, 3, 4, 5]

#test chop function
chop_list = test_list.copy()
chop(chop_list)
print('After chop:', chop_list)

middle_list = middle(test_list)
print('middle of the list:', middle_list)
