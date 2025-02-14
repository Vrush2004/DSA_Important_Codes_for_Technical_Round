# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # This stores all the generated permutations
        
        def backtrack(path, remaining):
            if not remaining:  # If no elements are left to add
                result.append(path[:])  # Store a copy of path
                return
            
            for i in range(len(remaining)):  # Iterate over remaining numbers
                path.append(remaining[i])  # Choose an element
                backtrack(path, remaining[:i] + remaining[i+1:])  # Recur with remaining numbers
                path.pop()  # Undo the choice (backtracking)
        
        backtrack([], nums)  # Start with an empty path
        return result  # Return all the permutations