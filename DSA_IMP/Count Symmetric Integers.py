# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num: int) -> bool:
            s = str(num)
            if len(s) % 2 != 0:
                return False
            n = len(s) // 2
            return sum(map(int, s[:n])) == sum(map(int, s[n:]))
        
        count = 0
        for i in range(low, high + 1):
            if is_symmetric(i):
                count += 1
        return count