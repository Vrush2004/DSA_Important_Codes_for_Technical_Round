# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Time Complexity: O(n⋅m)
# Space Complexity: O(1)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with every string in the list
        for string in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:  # If prefix becomes empty, return ""
                    return ""
        
        return prefix