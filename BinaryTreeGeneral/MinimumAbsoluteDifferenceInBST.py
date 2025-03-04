# Input: root = [4,2,6,1,3]
# Output: 1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)  # Visit left subtree
            
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update previous node value
            
            inorder(node.right)  # Visit right subtree

        inorder(root)
        return self.min_diff