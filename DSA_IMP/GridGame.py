# Input: grid = [[2,5,4],[1,5,1]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 0 + 4 + 0 = 4 points.

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        
        # Compute prefix sums for both rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n
        
        # Fill prefix sums for the top row
        top_prefix[0] = grid[0][0]
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
        
        # Fill prefix sums for the bottom row
        bottom_prefix[0] = grid[1][0]
        for i in range(1, n):
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        
        # Minimize the maximum points the second robot can collect
        result = float('inf')
        
        for i in range(n):
            # Points left for the second robot
            top_left = top_prefix[n - 1] - top_prefix[i]
            bottom_left = bottom_prefix[i - 1] if i > 0 else 0
            
            # Max points second robot can collect for this division
            second_robot_points = max(top_left, bottom_left)
            
            # Minimize the maximum points for the second robot
            result = min(result, second_robot_points)
        
        return result