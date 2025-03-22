#!/usr/bin/python3

def small_number(elmnt):
    no = elmnt[0]
    itr = len(elmnt)
    index = 0
    for i in range(itr):
        if elmnt[i] < no:
            no = elmnt[i] 
            index = i

    return index

def selection_sort(element):
    sort_list = list()
    copy = element
    itr = len(copy)
    for i in range(0, itr):
        no = small_number(copy)
        sort_list.append(copy.pop(no))

    return sort_list


print(selection_sort([4,10,5,7,8,9,2,3,1,8,7,2,14]))
