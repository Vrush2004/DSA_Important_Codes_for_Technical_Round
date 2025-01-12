# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Two pointers
        max_area = 0  # Variable to store the maximum area
        
        while left < right:
            # Calculate the area
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer with the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area