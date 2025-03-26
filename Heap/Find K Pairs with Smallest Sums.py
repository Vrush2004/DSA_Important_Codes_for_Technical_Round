# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []
        
        # Initialize heap with the first pair from each nums1 element with the first element of nums2
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)
        
        # Extract k pairs with the smallest sum
        while k > 0 and min_heap:
            _, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            
            # If there's a next pair in nums2, push it into the heap
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result

# Example Usage
sol = Solution()
print(sol.kSmallestPairs([1,7,11], [2,4,6], 3))  # Output: [[1,2],[1,4],[1,6]]
print(sol.kSmallestPairs([1,1,2], [1,2,3], 2))  # Output: [[1,1],[1,1]]