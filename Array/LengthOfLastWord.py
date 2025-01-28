# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Time Complexity: O(n)
# Space Complexity:O(k)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces and split the string into words
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])