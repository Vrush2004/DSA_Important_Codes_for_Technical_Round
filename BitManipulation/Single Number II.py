# from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update ones and twos based on the current number.
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones