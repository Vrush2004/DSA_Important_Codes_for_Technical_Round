# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Example 1:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
                
        return True