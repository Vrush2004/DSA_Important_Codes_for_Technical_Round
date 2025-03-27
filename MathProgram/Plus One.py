# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and propagate carry
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No need to continue if no carry
            
            digits[i] = 0  # Set current digit to 0 and carry over
        
        # If all digits were 9, we need to add an extra 1 at the front
        return [1] + digits