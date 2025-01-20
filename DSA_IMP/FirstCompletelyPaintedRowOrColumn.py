from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Step 1: Map matrix values to their positions (row, col)
        value_to_position = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                value_to_position[mat[r][c]] = (r, c)

        # Step 2: Initialize row and column counters
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        # Step 3: Process arr to paint cells and track row/column completion
        for i, value in enumerate(arr):
            r, c = value_to_position[value]  # Get the row and column of the value
            row_count[r] += 1               # Increment the painted cells in the row
            col_count[c] += 1               # Increment the painted cells in the column
            
            # Check if this row or column is fully painted
            if row_count[r] == n or col_count[c] == m:
                return i  # Return the smallest index where a row/column is fully painted
        
        return -1  # If no row or column is fully painted, which shouldn't happen as per the problem constraints