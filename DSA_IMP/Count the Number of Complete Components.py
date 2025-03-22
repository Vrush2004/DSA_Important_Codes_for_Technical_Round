# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.

from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        # Create adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        complete_components = 0

        # DFS function to explore a component
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                component.add(curr)
                stack.extend(graph[curr] - visited)

        # Find all connected components
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)

                # Check if the component is complete
                k = len(component)
                edge_count = sum(len(graph[v]) for v in component) // 2
                if edge_count == (k * (k - 1)) // 2:
                    complete_components += 1

        return complete_components