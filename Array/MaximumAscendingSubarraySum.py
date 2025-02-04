# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]  # Initialize with the first element
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # If ascending, add to current sum
                current_sum += nums[i]
            else:  # If not, reset current sum
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        return max(max_sum, current_sum)  # Ensure the last subarray is considered