# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find connected components using BFS
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            component = {start}
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component.add(neighbor)
                        queue.append(neighbor)
            return component

        visited = set()
        components = []
        for node in range(1, n + 1):
            if node not in visited:
                components.append(bfs(node))

        # Step 3: Check if each component is bipartite and find max depth
        def bipartite_bfs(node):
            queue = deque([(node, 1)])  # (node, depth)
            depth = {node: 1}
            max_depth = 1

            while queue:
                curr, d = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor in depth:
                        if abs(depth[neighbor] - d) != 1:
                            return -1  # Not bipartite
                    else:
                        depth[neighbor] = d + 1
                        max_depth = max(max_depth, d + 1)
                        queue.append((neighbor, d + 1))

            return max_depth

        total_groups = 0
        for component in components:
            max_groups = -1
            for node in component:
                res = bipartite_bfs(node)
                if res == -1:
                    return -1
                max_groups = max(max_groups, res)
            total_groups += max_groups

        return total_groups