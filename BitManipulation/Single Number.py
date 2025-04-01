# Input: nums = [2,2,1]
# Output: 1

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR all numbers
        return result