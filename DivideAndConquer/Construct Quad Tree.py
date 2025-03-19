# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(x, y, size):
            """Check if all elements in the sub-grid are the same."""
            val = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != val:
                        return False
            return True
        
        def build(x, y, size):
            """Recursively construct the Quad-Tree."""
            if isUniform(x, y, size):  # Base case: Uniform grid
                return Node(grid[x][y] == 1, True)
            
            half = size // 2
            return Node(
                val=True,  # This value is not used when isLeaf=False
                isLeaf=False,
                topLeft=build(x, y, half),
                topRight=build(x, y + half, half),
                bottomLeft=build(x + half, y, half),
                bottomRight=build(x + half, y + half, half)
            )

        return build(0, 0, len(grid))  # Start from the full grid