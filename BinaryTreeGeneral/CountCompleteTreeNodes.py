# Input: root = [1,2,3,4,5,6]
# Output: 6

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Calculate the depth of the leftmost path
        def get_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)

        if left_depth == right_depth:  # Left subtree is a full binary tree
            return (1 << left_depth) + self.countNodes(root.right)
        else:  # Right subtree is a full binary tree but one level smaller
            return (1 << right_depth) + self.countNodes(root.left)