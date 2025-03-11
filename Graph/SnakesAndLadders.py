# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Step 1: Convert 2D board into 1D array following Boustrophedon order
        def get_1D_position(row, col):
            return (n - 1 - row) * n + (col if (n - 1 - row) % 2 == 0 else (n - 1 - col))

        cells = [-1] * (n * n + 1)  # Using 1-based indexing
        idx = 1
        for row in range(n):
            for col in range(n):
                r, c = (n - 1 - row, col) if row % 2 == 0 else (n - 1 - row, n - 1 - col)
                cells[idx] = board[r][c]
                idx += 1
        
        # Step 2: BFS to find shortest path
        queue = deque([(1, 0)])  # (current_position, moves)
        visited = set()
        
        while queue:
            pos, moves = queue.popleft()
            if pos == n * n:
                return moves  # Reached last square
            
            for next_pos in range(pos + 1, min(pos + 6, n * n) + 1):  # Dice roll range
                dest = cells[next_pos] if cells[next_pos] != -1 else next_pos
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1  # If we never reach n^2, return -1