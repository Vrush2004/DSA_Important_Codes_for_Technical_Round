# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

from collections import defaultdict
import math
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        max_count = 0

        for i in range(n):
            hash_map = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x2 - x1 == 0:
                    slope = float('inf')  # Vertical line
                elif y2 - y1 == 0:
                    slope = 0.0  # Horizontal line
                else:
                    slope = (y2 - y1) / (x2 - x1)

                hash_map[slope] += 1

            if hash_map:
                max_count = max(max_count, max(hash_map.values()))

        return max_count + 1  # Include the base point itself