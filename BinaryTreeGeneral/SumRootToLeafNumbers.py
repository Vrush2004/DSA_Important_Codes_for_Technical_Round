# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = [[] for _ in range(n)]
        
        # Build the adjacency list for the tree
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Find the path from Bob to the root (node 0)
        parent = [-1] * n
        queue = deque([bob])
        parent[bob] = bob
        
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if parent[neighbor] == -1:  # Not visited
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Compute when Bob reaches each node
        time_bob = [-1] * n
        time = 0
        node = 0  # Start from root and follow Bob's path
        while node != bob:
            time_bob[node] = time
            node = parent[node]
            time += 1
        time_bob[bob] = time
        
        # DFS to find Alice's maximum profit
        def dfs(node: int, parent: int, time_alice: int) -> int:
            income = amount[node]
            if time_bob[node] == -1 or time_alice < time_bob[node]:  # Alice reaches first
                pass
            elif time_alice == time_bob[node]:  # They reach at the same time
                income //= 2
            else:  # Bob reaches first, no income for Alice
                income = 0
            
            max_profit = float('-inf')
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    max_profit = max(max_profit, dfs(neighbor, node, time_alice + 1))
            
            return income + (max_profit if not is_leaf else 0)
        
        return dfs(0, -1, 0)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            if not node.left and not node.right:  # If it's a leaf node
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)