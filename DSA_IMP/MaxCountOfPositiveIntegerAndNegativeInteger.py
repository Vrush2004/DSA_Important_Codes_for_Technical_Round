# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = 0
        pos_count = 0

        for num in nums:
            if num < 0:
                neg_count += 1
            elif num > 0:
                pos_count += 1

        return max(neg_count, pos_count)