# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            """
            Returns a tuple (depth, LCA node).
            - depth: Maximum depth of the subtree rooted at `node`
            - LCA node: LCA of deepest leaves in that subtree
            """
            if not node:
                return (0, None)
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif left_depth < right_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)
        
        return dfs(root)[1]