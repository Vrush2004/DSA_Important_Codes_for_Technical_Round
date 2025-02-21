# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def backtrack(curr):
            if len(curr) == n:
                happy_strings.append(curr)
                return
            
            for ch in 'abc':
                if not curr or curr[-1] != ch:   
                    backtrack(curr + ch)
        
        backtrack("")
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""