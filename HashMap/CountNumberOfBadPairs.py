# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total_pairs = len(nums) * (len(nums) - 1) // 2  # Total pairs
        count_map = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            key = num - i  # Transforming the equation j - i == nums[j] - nums[i] => nums[i] - i should be equal
            good_pairs += count_map[key]  # Count how many times we've seen this key before
            count_map[key] += 1  # Increment the count
        
        return total_pairs - good_pairs  # Bad pairs = total pairs - good pairs