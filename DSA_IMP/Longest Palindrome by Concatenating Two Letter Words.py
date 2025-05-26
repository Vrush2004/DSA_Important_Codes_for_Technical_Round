# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

class Solution(object):
    def longestPalindrome(self, words):
        mpp = Counter(words)
        count = 0
        alreadyPalindrome = 0
        for w, freq in mpp.items():
            s = w[::-1]
            if w == s:
                count += (freq // 2) * 4
                if freq % 2:
                    alreadyPalindrome = 1
            elif w < s and s in mpp:
                count += min(freq, mpp[s]) * 4
        return count + alreadyPalindrome * 2