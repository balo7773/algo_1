#!/usr/bin/python3

def quicksort(elements):
    if len(elements) < 2:
        return elements

    pivot = elements[0]
    less = []
    greater = []
    for i in elements[1:]:
        if i <= pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5,7,1,4,2,9,3,0,22,11,12,7,8]))
