# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph and in-degree array
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        # Initialize queue with courses having zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken_courses = 0
        
        while queue:
            course = queue.popleft()
            taken_courses += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return taken_courses == numCourses