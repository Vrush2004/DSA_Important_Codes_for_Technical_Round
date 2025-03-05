# Input: n = 1
# Output: 1
# Explanation: After 1 minute, there is only 1 blue cell, so we return 1.

class Solution:
    def coloredCells(self, n: int) -> int:
        return n * n + (n - 1) * (n - 1)