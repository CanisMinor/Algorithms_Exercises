# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] == x:
            return mid
    
    return -1


data = [8, 1, 23, 1, 11]
for b in data:
    print(binary_search([1, 5, 8, 12, 13], b))
