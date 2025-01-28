# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: If out of bounds or cell is land (0), return 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            # Catch the fish at the current cell and mark it as visited by setting it to 0
            fish = grid[r][c]
            grid[r][c] = 0
            
            # Explore all adjacent cells (up, down, left, right)
            fish += dfs(r + 1, c)
            fish += dfs(r - 1, c)
            fish += dfs(r, c + 1)
            fish += dfs(r, c - 1)
            
            return fish
        
        max_fish = 0
        
        # Iterate through all cells in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If the cell is a water cell, calculate the total fish that can be caught
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish