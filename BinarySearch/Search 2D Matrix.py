# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: 
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, n)  # Get row and column index
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False