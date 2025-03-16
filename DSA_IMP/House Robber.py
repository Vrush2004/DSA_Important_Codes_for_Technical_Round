# Input: nums = [2,3,5,9], k = 2
# Output: 5
# Explanation: 
# There are three ways to rob at least 2 houses:
# - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
# - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
# - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
# Therefore, we return min(5, 9, 9) = 5.

from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        
        def canRob(cap):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:  # If we can rob this house
                    count += 1
                    i += 1  # Skip the adjacent house
                i += 1  # Move to the next house
            return count >= k  # Check if we can rob at least k houses
        
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):  # If it's possible to rob k houses with this capability
                right = mid  # Try for a smaller capability
            else:
                left = mid + 1  # Increase capability

        return left  # Minimum capability required