# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0  # Not enough candies for each child to get at least 1

        left, right = 1, max(candies)
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)  # Number of children we can serve
            
            if count >= k:
                best = mid  # Store the best possible answer
                left = mid + 1  # Try for a larger value
            else:
                right = mid - 1  # Reduce the number of candies per child

        return best