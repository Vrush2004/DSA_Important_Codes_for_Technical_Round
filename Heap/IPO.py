# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

from heapq import heappop, heappush
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))  # Sort projects by required capital
        max_heap = []
        i = 0
        n = len(profits)

        for _ in range(k):
            # Add all projects that can be started with current capital
            while i < n and projects[i][0] <= w:
                heappush(max_heap, -projects[i][1])  # Max heap (store negative values)
                i += 1
            
            if not max_heap:
                break  # No more projects can be started
            
            w += -heappop(max_heap)  # Pick the most profitable project

        return w