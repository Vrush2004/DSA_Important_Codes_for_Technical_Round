# Input: nums = [1,4,3,3,2]
# Output: 2
# Explanation:
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
# Hence, we return 2.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        inc = dec = 1  # Start with at least 1 element in a subarray
        max_length = 1  # The minimum valid answer is 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc += 1
                dec = 1  # Reset decreasing counter
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec += 1
                inc = 1  # Reset increasing counter
            else:  # Equal elements break both sequences
                inc = dec = 1
            
            max_length = max(max_length, inc, dec)
        
        return max_length