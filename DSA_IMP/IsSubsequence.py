# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for both strings
        i, j = 0, 0
        # Lengths of both strings
        len_s, len_t = len(s), len(t)

        # Traverse the target string `t`
        while i < len_s and j < len_t:
            # If characters match, move the pointer for `s`
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for `t`
            j += 1

        # If we've matched all characters in `s`, return True
        return i == len_s