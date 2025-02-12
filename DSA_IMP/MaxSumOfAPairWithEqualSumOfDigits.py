# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.

from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        sum_map = {}
        max_sum = -1
        
        for num in nums:
            s = digit_sum(num)
            if s in sum_map:
                max_sum = max(max_sum, sum_map[s] + num)
                sum_map[s] = max(sum_map[s], num)
            else:
                sum_map[s] = num
        
        return max_sum