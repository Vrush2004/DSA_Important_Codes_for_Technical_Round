# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Precompute a prefix sum array to count words starting and ending with vowels
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        # Answer each query using the prefix sum array
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])
        
        return result