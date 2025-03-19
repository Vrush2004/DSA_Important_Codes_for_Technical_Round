# Input: nums = [0,1,1,1,0,0]
# Output: 3
# Explanation:
# We can do the following operations:
# Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
# Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
# Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):  # We check up to n-2 to ensure a triplet exists
            if nums[i] == 0:  # Flip only when encountering a 0
                operations += 1
                # Flip the next three elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        
        # Check if the array is fully 1s
        return operations if all(x == 1 for x in nums) else -1