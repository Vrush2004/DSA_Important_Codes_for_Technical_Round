# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_count = {}
        repeated = -1
        missing = -1

        # Flatten grid and count occurrences
        for row in grid:
            for num in row:
                if num in num_count:
                    repeated = num
                num_count[num] = num_count.get(num, 0) + 1

        # Find the missing number
        for i in range(1, n * n + 1):
            if i not in num_count:
                missing = i
                break
        
        return [repeated, missing]