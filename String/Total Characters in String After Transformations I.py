# Input: s = "abcyy", t = 2
# Output: 7
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        # Initialize count of characters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(25):  # a to y
                new_count[i + 1] += count[i]
            # handle 'z' -> 'a' + 'b'
            new_count[0] += count[25]
            new_count[1] += count[25]
            count = new_count

        return sum(count) % MOD