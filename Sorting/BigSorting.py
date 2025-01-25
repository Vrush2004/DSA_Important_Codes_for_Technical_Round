#!/bin/python3

import os

def bigSorting(unsorted):
    # Convert the strings into integers for comparison
    n = len(unsorted)
    
    # Bubble sort implementation
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare by length first, then lexicographically if lengths are the same
            if (len(unsorted[j]) > len(unsorted[j + 1]) or
                (len(unsorted[j]) == len(unsorted[j + 1]) and unsorted[j] > unsorted[j + 1])):
                # Swap if the condition is true
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
    
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()