# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:  # Move left if target found
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:  # Move right if target found
                    if nums[mid] == target:
                        last = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        first = findFirst(nums, target)
        if first == -1:  # If target not found, return [-1, -1]
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]