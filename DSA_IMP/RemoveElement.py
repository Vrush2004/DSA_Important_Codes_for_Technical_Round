# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the position to place valid elements
        k = 0
        
        # Iterate over the nums array
        for i in range(len(nums)):
            # If the element is not equal to val, place it in the next position of nums[k]
            if nums[i] != val:
                nums[k] = nums[i]  # Put the element at the position k
                k += 1  # Move the pointer to the next position
        
        # Return the length of the array without the val elements
        return k