# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Helper function to find primes up to a limit using Sieve of Eratosthenes
        def sieve(limit: int):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            return is_prime
        
        # Generate primes up to 'right'
        is_prime = sieve(right)
        
        # Extract primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # If less than two primes exist, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]
        
        # Find the closest prime pair
        min_diff = float('inf')
        ans = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
        
        return ans