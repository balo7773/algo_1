#!/usr/bin/python3

def sum(elements):
    copy = elements
    if len(copy) == 1:
        return copy[0]
    return copy[0] + sum(copy[1:])

test_case = [0,2,7,10,9,6,22,8,5]

def count(elements):
    if len(elements) == 1:
        return 1
    elif len(elements) == 0:
        return 0

    return 1 + count(elements[1:])

#print(count(test_case))

def max_no(elements):
    if len(elements) == 1:
        return elements[0]
    return elements[0] if elements[0] > max_no(elements[1:]) else max_no(elements[1:])
#print(max_no(test_case))

def binary_search(no, elements):
    low = 0
    high = len(elements) - 1
    mid = (low + high) // 2
    if mid == 0:
        return no
    if no > elements[mid]:
        return binary_search(no, elements[mid + 1 :])
    elif no < elements[mid]:
        return binary_search(no, elements[: mid])
    elif no == elements[mid]:
        return 'found'

print(binary_search(5, [1,2,3,4,5,6,7,8,9,10,11,12,13]))
