#!/bin/python3

import os

def cost(B):
    n = len(B)
    
    # Initialize low and high for the first element
    low = 0
    high = 0

    for i in range(1, n):
        # Compute new values for low and high
        new_low = max(low, high + abs(B[i - 1] - 1))
        new_high = max(low + abs(B[i] - 1), high + abs(B[i] - B[i - 1]))

        # Update low and high
        low = new_low
        high = new_high

    # Return the maximum cost
    return max(low, high)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        B = list(map(int, input().rstrip().split()))
        result = cost(B)
        fptr.write(str(result) + '\n')

    fptr.close()