# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid + 1]:  
                high = mid  # Move left
            else:
                low = mid + 1  # Move right
        
        return low  # or return high (both will be the same)