# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            if len(path) == k:  # If combination size reaches k, add to result
                result.append(path[:])
                return
            
            for i in range(start, n + 1):  # Choose numbers sequentially
                path.append(i)
                backtrack(i + 1, path)  # Recur with the next number
                path.pop()  # Backtrack to try other numbers
        
        backtrack(1, [])  # Start with an empty combination
        return result