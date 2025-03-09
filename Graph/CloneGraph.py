# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}  # Dictionary to store cloned nodes

        def dfs(original):
            if original in visited:
                return visited[original]  # Return already cloned node

            # Clone current node
            clone = Node(original.val)
            visited[original] = clone  # Mark as visited
            
            # Clone neighbors recursively
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)  # Start DFS from the given node