# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        # Arrays to store the maximum height to the left and right of each index
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]
        
        return trapped_water
    

# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Add all boundary cells to the heap and mark them as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Directions for 4 adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water_trapped = 0
        
        # Process the min-heap
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            
            # Check all 4 neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and hasn't been visited
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # If the current height is higher, it can trap water
                    if heightMap[nx][ny] < height:
                        water_trapped += height - heightMap[nx][ny]
                    # Add the neighbor to the heap with the max height between current and neighbor
                    heapq.heappush(min_heap, (max(heightMap[nx][ny], height), nx, ny))
        
        return water_trapped