# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.

from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        qlen = len(queries)
        answer = [0] * qlen
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        min_heap = [(grid[0][0], 0, 0)]  # Min-heap with (value, x, y)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        
        for index, query in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                val, x, y = heappop(min_heap)
                count += 1
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heappush(min_heap, (grid[nx][ny], nx, ny))
            
            answer[index] = count
        
        return answer