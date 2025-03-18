# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        mask = 0
        max_len = 0
        
        for right in range(len(nums)):
            # While the AND condition is violated, remove elements from the left
            while (mask & nums[right]) != 0:
                mask ^= nums[left]  # Remove leftmost element
                left += 1
            
            # Include the new element
            mask |= nums[right]
            max_len = max(max_len, right - left + 1)
        
        return max_len