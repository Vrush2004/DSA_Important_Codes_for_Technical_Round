# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

class Solution:
    def maxScore(self, s: str) -> int:
        # Step 1: Initialize the total number of ones in the string
        ones_count = s.count('1')
        
        # Step 2: Initialize variables to track the count of zeros on the left
        # and ones on the right
        left_zeros = 0
        right_ones = ones_count
        max_score = 0
        
        # Step 3: Iterate over the string and calculate the score for each split point
        for i in range(len(s) - 1):  # We stop at len(s) - 1 to ensure both parts are non-empty
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            # Calculate the score for this split
            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)
        
        return max_score