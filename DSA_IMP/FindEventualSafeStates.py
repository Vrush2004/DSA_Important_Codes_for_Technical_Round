# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        
        # Reverse the graph and calculate in-degrees
        for src in range(n):
            for dest in graph[src]:
                reverse_graph[dest].append(src)
                in_degree[src] += 1
        
        # Queue for nodes with in-degree 0 (terminal nodes initially)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []
        
        # Process the queue
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Return safe nodes sorted in ascending order
        return sorted(safe_nodes)