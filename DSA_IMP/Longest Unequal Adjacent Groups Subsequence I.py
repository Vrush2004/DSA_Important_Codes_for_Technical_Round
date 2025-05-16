# Input: words = ["e","a","b"], groups = [0,0,1]
# Output: ["e","b"]
# Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []

        result = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result