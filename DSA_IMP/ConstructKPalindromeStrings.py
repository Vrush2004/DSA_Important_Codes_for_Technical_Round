# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of s, it's impossible
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # Check if the number of palindromes is feasible
        return odd_count <= k