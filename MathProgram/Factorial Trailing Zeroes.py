# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count