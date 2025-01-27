# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count the characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Initialize pointers and variables
        left, right = 0, 0
        formed = 0
        window_count = {}
        
        # Result tuple to store the length of the window and its start and end positions
        res = float("inf"), None, None
        
        while right < len(s):
            # Add the current character to the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the current character matches the count in t, increment `formed`
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window if all characters are satisfied
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if this window is smaller
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)
                
                # Remove the character at the left pointer
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                # Move the left pointer
                left += 1
            
            # Expand the window by moving the right pointer
            right += 1
        
        # Return the smallest window or an empty string if no such window exists
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]