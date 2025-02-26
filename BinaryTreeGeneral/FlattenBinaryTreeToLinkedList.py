# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node of left subtree
                pre = curr.left
                while pre.right:
                    pre = pre.right
                # Connect rightmost node to the right subtree
                pre.right = curr.right
                # Move left subtree to the right
                curr.right = curr.left
                curr.left = None
            # Move to next right node
            curr = curr.right