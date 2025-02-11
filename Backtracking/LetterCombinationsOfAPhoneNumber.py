# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # Edge case: Empty input
            return []
        
        # Digit to letter mapping
        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, path: str):
            # If we have formed a combination of the same length as digits, store it
            if index == len(digits):
                result.append(path)
                return
            
            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Recursively explore each possibility
            for letter in possible_letters:
                backtrack(index + 1, path + letter)
        
        # Start backtracking from index 0 with an empty path
        backtrack(0, "")
        
        return result