# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If strings are already equal, return True
        if s1 == s2:
            return True
        
        # Find indices where characters differ
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        
        # There should be exactly two differences, and swapping should fix it
        return len(diff) == 2 and diff[0] == diff[1][::-1]