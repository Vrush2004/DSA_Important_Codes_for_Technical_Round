# Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
# Output: 1
# Explanation:
# After removing queries[2], nums can still be converted to a zero array.
# Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
# Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

from typing import List
from collections import defaultdict

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        def is_possible(removed_set):
            coverage = [0] * n
            for i, (l, r) in enumerate(queries):
                if i in removed_set:
                    continue
                for j in range(l, r + 1):
                    coverage[j] += 1
            for i in range(n):
                if coverage[i] < nums[i]:
                    return False
            return True

        # First check if even with all queries it's possible
        if not is_possible(set()):
            return -1

        # Try to remove maximum queries
        left, right = 0, len(queries)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            # Try all combinations of removing 'mid' queries (not efficient -> optimize)
            found = False
            from itertools import combinations
            for remove_set in combinations(range(len(queries)), mid):
                if is_possible(set(remove_set)):
                    found = True
                    break
            if found:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer