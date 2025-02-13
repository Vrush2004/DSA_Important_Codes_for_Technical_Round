# Input: nums = [2,11,10,1,3], k = 10
# Output: 2
# Explanation: In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3].
# In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums. nums becomes equal to [10, 11, 10].
# At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
# It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while nums[0] < k:  # Check if the smallest element is still < k
            x = heappop(nums)  # Smallest element
            y = heappop(nums)  # Second smallest element
            new_val = min(x, y) * 2 + max(x, y)
            heappush(nums, new_val)  # Push the new value into the heap
            operations += 1  # Increment operation count

        return operations