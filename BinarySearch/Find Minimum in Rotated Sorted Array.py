# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:  
                left = mid + 1  # Minimum is in the right half
            else:
                right = mid  # Minimum is at mid or in the left half
        
        return nums[left]  # Left will point to the minimum element