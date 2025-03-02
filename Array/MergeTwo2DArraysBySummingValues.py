# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}
        
        for id1, val1 in nums1:
            merged[id1] = merged.get(id1, 0) + val1
        
        for id2, val2 in nums2:
            merged[id2] = merged.get(id2, 0) + val2
        
        return sorted([[id, val] for id, val in merged.items()])