# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # If needle is longer than haystack, it cannot be found
        if needle_len > haystack_len:
            return -1

        # Iterate through haystack
        for i in range(haystack_len - needle_len + 1):
            # Check if substring of haystack matches needle
            match = True
            for j in range(needle_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i  # Return the index if found
        
        return -1  # Return -1 if not found