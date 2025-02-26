# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum = 0, 0
        max_so_far, min_so_far = 0, 0
        
        for num in nums:
            max_so_far = max(0, max_so_far + num)
            min_so_far = min(0, min_so_far + num)
            max_sum = max(max_sum, max_so_far)
            min_sum = min(min_sum, min_so_far)
        
        return max(max_sum, abs(min_sum))