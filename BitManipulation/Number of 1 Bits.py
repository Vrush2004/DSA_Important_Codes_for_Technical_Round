# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Removes the rightmost 1-bit
            count += 1
        return count