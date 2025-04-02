# Input: left = 5, right = 7
# Output: 4

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        
        # Keep right-shifting until left == right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Now left == right, shift left back to its original position
        return left << shift