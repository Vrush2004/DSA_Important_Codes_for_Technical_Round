# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and go upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(
                    triangle[row + 1][col],
                    triangle[row + 1][col + 1]
                )
        
        return triangle[0][0]  # Top element contains the min total path sum