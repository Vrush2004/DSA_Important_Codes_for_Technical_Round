# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def custom_sort(s: str) -> str:
            # Counting sort for lowercase letters ('a' to 'z')
            count = [0] * 26  # Frequency array for 26 letters
            
            for char in s:
                count[ord(char) - ord('a')] += 1  # Increment frequency
            
            # Reconstruct sorted string based on frequency count
            sorted_str = ""
            for i in range(26):
                sorted_str += chr(i + ord('a')) * count[i]
            
            return sorted_str
        
        anagrams = defaultdict(list)
        
        for word in strs:
            sorted_word = custom_sort(word)  # Get sorted representation
            anagrams[sorted_word].append(word)  # Group anagrams
        
        return list(anagrams.values())  # Convert defaultdict to list