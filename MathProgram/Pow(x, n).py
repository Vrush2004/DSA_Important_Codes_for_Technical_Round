# Input: x = 2.00000, n = 10
# Output: 1024.00000

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        
        return result