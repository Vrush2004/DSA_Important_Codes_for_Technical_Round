# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
# Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
# Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
# Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Convert string to list of characters for easy modification
        s = list(s)
        
        # Initialize a list to track cumulative shifts
        shift_count = [0] * len(s)
        
        # Step 1: Apply the shifts to the shift_count array
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                shift_count[start] += 1
                if end + 1 < len(s):
                    shift_count[end + 1] -= 1
            else:  # Backward shift
                shift_count[start] -= 1
                if end + 1 < len(s):
                    shift_count[end + 1] += 1
        
        # Step 2: Calculate cumulative shifts using prefix sum
        current_shift = 0
        for i in range(len(s)):
            current_shift += shift_count[i]
            
            # Apply the shift to the character (consider wrapping around)
            new_char = chr(((ord(s[i]) - ord('a') + current_shift) % 26) + ord('a'))
            s[i] = new_char
        
        # Convert list back to string and return
        return ''.join(s)

# Example usage:
sol = Solution()

s1 = "abc"
shifts1 = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(sol.shiftingLetters(s1, shifts1))  # Output: "ace"

s2 = "dztz"
shifts2 = [[0, 0, 0], [1, 1, 1]]
print(sol.shiftingLetters(s2, shifts2))  # Output: "catz"