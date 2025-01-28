# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right across the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move the top boundary down
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left
            
            if top <= bottom:
                # Traverse from right to left across the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right
        
        return result