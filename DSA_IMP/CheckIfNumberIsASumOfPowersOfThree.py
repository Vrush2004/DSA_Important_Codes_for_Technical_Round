# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True