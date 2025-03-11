# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create adjacency list and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        # Step 2: Populate adjacency list and in-degree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Step 3: Add courses with in-degree 0 to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        # Step 4: Process courses in queue
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check if ordering is possible (all courses should be taken)
        return order if len(order) == numCourses else []