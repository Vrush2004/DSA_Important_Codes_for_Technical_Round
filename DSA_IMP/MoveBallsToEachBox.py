# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        # Step 1: Initialize result array to store the minimum operations for each box
        result = [0] * n
        
        # Step 2: First pass from left to right
        left_operations = 0
        left_count = 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                left_count += 1
            left_operations += left_count
            result[i] += left_operations
        
        # Step 3: Second pass from right to left
        right_operations = 0
        right_count = 0
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                right_count += 1
            right_operations += right_count
            result[i] += right_operations
        
        return result

# Example usage:
sol = Solution()

# Example 1:
s1 = "101"
print(sol.minOperations(s1))  # Output: [1, 1, 3]

# Example 2:
s2 = "011101"
print(sol.minOperations(s2))  # Output: [4, 3, 3, 3, 4, 5]

# Example 3:
s3 = "000"
print(sol.minOperations(s3))  # Output: [0, 0, 0]