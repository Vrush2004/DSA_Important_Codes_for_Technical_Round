# Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# Output: 1
# Explanation: 
# There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
# Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.

from bisect import bisect_left
from sortedcontainers import SortedList
from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Step 1: Create position map for nums1
        pos_in_nums1 = {val: idx for idx, val in enumerate(nums1)}
        
        # Step 2: Transform nums2 into positions based on nums1
        transformed = [pos_in_nums1[val] for val in nums2]
        
        # Step 3: Count good triplets using two passes with a Fenwick Tree (or Binary Indexed Tree)
        
        # First pass to count how many smaller elements are to the left of each element
        left_count = [0] * n
        fenwick_tree = [0] * (n + 1)
        
        def update(index, delta):
            while index <= n:
                fenwick_tree[index] += delta
                index += index & -index
        
        def query(index):
            sum_val = 0
            while index > 0:
                sum_val += fenwick_tree[index]
                index -= index & -index
            return sum_val
        
        for i in range(n):
            val = transformed[i]
            left_count[i] = query(val)
            update(val + 1, 1)  # increment the position in Fenwick Tree
        
        # Second pass to count how many greater elements are to the right of each element
        right_count = [0] * n
        fenwick_tree = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            val = transformed[i]
            right_count[i] = query(n) - query(val)
            update(val + 1, 1)  # increment the position in Fenwick Tree
        
        # Step 4: Count all good triplets
        total_triplets = 0
        for i in range(n):
            total_triplets += left_count[i] * right_count[i]
        
        return total_triplets