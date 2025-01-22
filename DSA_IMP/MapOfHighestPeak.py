# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        # Initialize the height matrix with -1 (unvisited)
        height = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Add all water cells to the queue and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        # Directions for moving to adjacent cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS to calculate heights
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and if the neighbor is unvisited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        
        return height