#!/bin/python3

import os

def getWays(n, c):
    # Create a DP array initialized with zeros
    dp = [0] * (n + 1)
    # Base case: There is one way to make change for 0 (no coins used)
    dp[0] = 1

    # Iterate over each coin
    for coin in c:
        # Update DP array for each amount from the coin value to n
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    # The answer is the number of ways to make change for n
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()