# Input: words = ["bab","dab","cab"], groups = [1,2,2]
# Output: ["bab","cab"]
# Explanation: A subsequence that can be selected is [0,2].
# groups[0] != groups[2]
# words[0].length == words[2].length, and the hamming distance between them is 1.
# So, a valid answer is [words[0],words[2]] = ["bab","cab"].
# Another subsequence that can be selected is [0,1].
# groups[0] != groups[1]
# words[0].length == words[1].length, and the hamming distance between them is 1.
# So, another valid answer is [words[0],words[1]] = ["bab","dab"].
# It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1