# Input: nums = [1,2,3,1], k = 3
# Output: true

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}  # Dictionary to store the last seen index of each number
        
        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True  # Found duplicate within the given range
            num_indices[num] = i  # Update the last seen index of the number
        
        return False  # No valid duplicate found