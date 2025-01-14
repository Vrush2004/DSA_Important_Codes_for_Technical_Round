# Input: s = "abaacbcbb"
# Output: 5
# Explanation:
# We do the following operations:
# Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
# Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".

class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Count the frequency of each character in the string
        charFrequencyMap = {}
        for currentChar in s:
            charFrequencyMap[currentChar] = charFrequencyMap.get(currentChar, 0) + 1

        # Step 2: Calculate the number of characters to delete
        deleteCount = 0
        for frequency in charFrequencyMap.values():
            if frequency % 2 == 1:
                # If frequency is odd, delete all except one
                deleteCount += frequency - 1
            else:
                # If frequency is even, delete all except two
                deleteCount += frequency - 2

        # Step 3: Return the minimum length after deletions
        return len(s) - deleteCount
