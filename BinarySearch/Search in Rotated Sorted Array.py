# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Calculate mid index

            if nums[mid] == target:  
                return mid  # Target found at index mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1  # Target is in the left sorted half
                else:
                    left = mid + 1  # Target is in the right half
            
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1  # Target is in the right sorted half
                else:
                    right = mid - 1  # Target is in the left half
        
        return -1  # Target not found