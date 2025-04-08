# Input: nums = [1,2,3,4,2,3,3,5,7]
# Output: 2
# Explanation:
# In the first operation, the first 3 elements are removed, resulting in the array [4, 2, 3, 3, 5, 7].
# In the second operation, the next 3 elements are removed, resulting in the array [3, 5, 7], which has distinct elements.
# Therefore, the answer is 2.

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) != len(set(nums)):
            # Remove the first 3 elements or all if fewer than 3
            nums = nums[3:] if len(nums) >= 3 else []
            operations += 1
        return operations