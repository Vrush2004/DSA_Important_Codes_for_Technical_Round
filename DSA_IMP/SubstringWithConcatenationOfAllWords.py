# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation:
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])  # Length of each word
        total_len = word_len * len(words)  # Total length of the concatenated substring
        word_count = Counter(words)  # Count of words in the words list
        n = len(s)  # Length of the input string
        result = []

        for i in range(word_len):  # Loop through each possible starting position
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= n:  # Ensure we don't go out of bounds
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:  # If the word is in the target list
                    current_count[word] += 1

                    # If the word occurs more than expected, move the left pointer
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len

                    # If the window matches the target, record the starting index
                    if right - left == total_len:
                        result.append(left)

                else:  # Reset the window if the word is not in the target list
                    current_count.clear()
                    left = right

        return result