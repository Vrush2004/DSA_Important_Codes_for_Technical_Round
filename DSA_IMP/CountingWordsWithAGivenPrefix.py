# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        for word in words:
            # Check if the word starts with the prefix
            if word.startswith(pref):
                count += 1
        
        return count