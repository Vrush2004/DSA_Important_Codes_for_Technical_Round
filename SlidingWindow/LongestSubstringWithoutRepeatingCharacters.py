# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        char_set = set()
        left = 0
        max_length = 0

        # Use the sliding window approach
        for right in range(len(s)):
            # If a duplicate character is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length