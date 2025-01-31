# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        island_sizes = {}
        index = 2  # Start indexing islands from 2 to distinguish from water (0) and land (1)

        def dfs(r, c, index):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = index
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, index)
            return size

        # Step 1: Identify all islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[index] = dfs(r, c, index)
                    index += 1

        # If there's no 0 to flip, return the size of the largest island
        if not island_sizes:
            return n * n

        max_area = max(island_sizes.values())  # Get the largest island found so far

        # Step 2: Try flipping each 0 and calculate the largest possible island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_area = 1  # Start with 1 because we are flipping this 0 to 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])

                    for island in seen:
                        new_area += island_sizes[island]

                    max_area = max(max_area, new_area)

        return max_area