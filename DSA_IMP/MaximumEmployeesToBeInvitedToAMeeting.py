# Input: favorite = [2,2,1,2]
# Output: 3
# Explanation:
# The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
# All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
# Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
# The maximum number of employees that can be invited to the meeting is 3. 

from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for i in range(n):
            indegree[favorite[i]] += 1

        # Step 1: Identify all nodes not part of a cycle using a topological sort
        queue = deque([i for i in range(n) if indegree[i] == 0])
        chain_length = [0] * n
        
        while queue:
            node = queue.popleft()
            neighbor = favorite[node]
            chain_length[neighbor] = max(chain_length[neighbor], chain_length[node] + 1)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

        # Step 2: Process cycles and chains leading to mutual favorite pairs
        visited = [False] * n
        max_cycle_size = 0
        total_chain_length = 0

        for i in range(n):
            if indegree[i] > 0:  # Node is part of a cycle
                cycle_size = 0
                current = i
                while not visited[current]:
                    visited[current] = True
                    current = favorite[current]
                    cycle_size += 1
                if cycle_size == 2:  # Mutual favorite pair
                    # Add chains leading to the mutual favorite pair
                    total_chain_length += 2 + chain_length[i] + chain_length[favorite[i]]
                else:
                    max_cycle_size = max(max_cycle_size, cycle_size)

        # Step 3: Return the maximum between chains + mutual favorites and the largest cycle
        return max(max_cycle_size, total_chain_length)