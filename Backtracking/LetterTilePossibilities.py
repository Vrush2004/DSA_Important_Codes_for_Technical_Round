# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letter_count = Counter(tiles)
        result = set()  
        
        def backtrack(path):
            if path:
                result.add(path)  
            
            for letter in list(letter_count):  
                if letter_count[letter] > 0:  
                    letter_count[letter] -= 1  
                    backtrack(path + letter)  
                    letter_count[letter] += 1  

        backtrack("")  
        return len(result)  

sol = Solution()
print(sol.numTilePossibilities("AAB"))  # Output: 8
print(sol.numTilePossibilities("AAABBC"))  # Output: 188
print(sol.numTilePossibilities("V"))  # Output: 1