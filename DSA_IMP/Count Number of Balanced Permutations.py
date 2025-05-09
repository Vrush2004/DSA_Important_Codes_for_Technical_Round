# Input: num = "123"
# Output: 2
# Explanation:
# The distinct permutations of num are "123", "132", "213", "231", "312" and "321".
# Among them, "132" and "231" are balanced. Thus, the answer is 2.

from itertools import permutations

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        velunexorai = num  # store input midway
        
        # Use a set to avoid duplicate permutations
        seen = set(permutations(velunexorai))
        count = 0

        for perm in seen:
            even_sum = sum(int(perm[i]) for i in range(0, len(perm), 2))
            odd_sum = sum(int(perm[i]) for i in range(1, len(perm), 2))
            if even_sum == odd_sum:
                count += 1

        return count % MOD
