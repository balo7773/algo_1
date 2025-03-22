#!/usr/bin/python3

def binary_search(element, search_element):
    low = 0
    high = len(element) - 1

    while low <= high:
        mid = (low + high) // 2
        if search_element > element[mid]:
            low = mid + 1
        elif search_element < element[mid]:
            high = mid - 1
        elif search_element == element[mid]:
            return 'found'
        else:
            return 'not found'

    return

element = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_element = 30
# Expected output: 'found'

print(binary_search(element, search_element))
