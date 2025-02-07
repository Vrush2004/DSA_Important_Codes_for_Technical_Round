# Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
# Output: [1,2,2,3]
# Explanation:
# After query 0, ball 1 has color 4.
# After query 1, ball 1 has color 4, and ball 2 has color 5.
# After query 2, ball 1 has color 3, and ball 2 has color 5.
# After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Dictionary to store the color of each ball
        color_count = defaultdict(int)  # Dictionary to track occurrences of each color
        unique_colors = 0  # Counter for distinct colors
        result = []

        for x, y in queries:
            if x in ball_colors:
                prev_color = ball_colors[x]
                color_count[prev_color] -= 1
                # If the previous color is no longer used, reduce unique color count
                if color_count[prev_color] == 0:
                    unique_colors -= 1
            
            # Assign the new color to the ball
            ball_colors[x] = y
            # If the new color was not used before, increase unique color count
            if color_count[y] == 0:
                unique_colors += 1
            color_count[y] += 1

            result.append(unique_colors)  # Store the count of unique colors
        
        return result