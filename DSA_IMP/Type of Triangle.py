# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        
        # Check for triangle validity using triangle inequality theorem
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "none"
        
        # Check for equilateral
        if a == b == c:
            return "equilateral"
        
        # Check for isosceles (exactly two sides equal)
        if a == b or b == c or a == c:
            return "isosceles"
        
        # Otherwise scalene (all sides different)
        return "scalene"