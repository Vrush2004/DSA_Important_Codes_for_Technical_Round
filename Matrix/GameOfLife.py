# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Directions for the 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1), (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        
        # Step 1: First pass - Encode the next state in-place
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live_neighbors += 1
                
                # Apply rules:
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Mark live -> dead (1 -> 0) using -1
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # Mark dead -> live (0 -> 1) using 2
        
        # Step 2: Second pass - Final conversion
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1