from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        
        def recover(node: Optional[TreeNode], val: int):
            if not node:
                return
            node.val = val
            self.values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)
        
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_max = max(helper(node.left), 0)
            right_max = max(helper(node.right), 0)
            
            self.max_sum = max(self.max_sum, left_max + right_max + node.val)
            
            return node.val + max(left_max, right_max)
        
        helper(root)
        return self.max_sum