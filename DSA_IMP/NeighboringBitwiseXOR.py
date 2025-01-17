# Input: derived = [1,1,0]
# Output: true
# Explanation: A valid original array that gives derived is [0,1,0].
# derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
# derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
# derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0

from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # Try original[0] = 0
        original = [0] * n
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]
        if original[-1] ^ original[0] == derived[-1]:
            return True
        
        # Try original[0] = 1
        original = [1] * n
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]
        if original[-1] ^ original[0] == derived[-1]:
            return True
        
        return False