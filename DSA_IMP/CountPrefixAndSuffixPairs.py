# Input: words = ["a","aba","ababa","aa"]
# Output: 4
# Explanation: In this example, the counted index pairs are:
# i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
# i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
# i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
# i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
# Therefore, the answer is 4.

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            return str2.startswith(str1) and str2.endswith(str1)
        
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):  # Ensure i < j
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count