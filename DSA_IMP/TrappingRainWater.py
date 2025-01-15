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