# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}  # Dictionary to store parent of each node

        # Find function with path compression
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        # Union function with union by rank
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False  # Cycle detected
            parent[root2] = root1  # Union
            return True

        # Initialize each node as its own parent
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

            if not union(u, v):
                return [u, v]  # Return the redundant edge