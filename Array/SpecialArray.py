# Input: nums = [4,3,1,6]
# Output: false
# Explanation:
# nums[1] and nums[2] are both odd. So the answer is false.

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:  # Check if both are even or both are odd
                return False
        return True