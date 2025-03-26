# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        nums = [num for row in grid for num in row]
        
        # Check if all elements have the same remainder modulo x
        remainder = nums[0] % x
        if any(num % x != remainder for num in nums):
            return -1
        
        # Convert numbers to "steps" required to reach the median
        nums = [num // x for num in nums]
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Compute minimum operations
        return sum(abs(num - median) for num in nums)

# Example Usage
sol = Solution()
print(sol.minOperations([[2,4],[6,8]], 2))  # Output: 4
print(sol.minOperations([[1,5],[2,3]], 1))  # Output: 5
print(sol.minOperations([[1,2],[3,4]], 2))  # Output: -1