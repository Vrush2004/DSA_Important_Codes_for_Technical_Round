# Input: nums = [1,2,1,2,1,1,1]
# Output: 5
# Explanation: 
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.
# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode

from math import gcd
from functools import reduce
from typing import List

class Solution:
    def lcm(self, a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)

    def lcm_of_list(self, arr: List[int]) -> int:
        return reduce(self.lcm, arr, 1)

    def gcd_of_list(self, arr: List[int]) -> int:
        return reduce(gcd, arr, 0)

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate over all subarrays
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j + 1]
                prod = 1
                for num in subarray:
                    prod *= num
                
                lcm_value = self.lcm_of_list(subarray)
                gcd_value = self.gcd_of_list(subarray)
                
                # Check the product equivalence condition
                if prod == lcm_value * gcd_value:
                    max_len = max(max_len, len(subarray))
        
        return max_len