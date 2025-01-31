# Input: s = "anagram", t = "nagaram"
# Output: true

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)