# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)  # Remove smallest element
        
        return min_heap[0]  # Kth largest element

# Example Usage
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4