# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, nums[0]  # dp[i-2] and dp[i-1]
        
        for i in range(1, len(nums)):
            current = max(prev1, nums[i] + prev2)
            prev2, prev1 = prev1, current
        
        return prev1