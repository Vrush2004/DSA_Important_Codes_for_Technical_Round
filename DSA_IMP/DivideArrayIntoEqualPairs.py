# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return all(v % 2 == 0 for v in count.values())