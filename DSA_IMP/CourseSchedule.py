# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize the graph matrix
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Populate direct prerequisites
        for a, b in prerequisites:
            is_prerequisite[a][b] = True
        
        # Floyd-Warshall algorithm to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_prerequisite[i][j] = is_prerequisite[i][j] or (is_prerequisite[i][k] and is_prerequisite[k][j])
        
        # Answer the queries
        return [is_prerequisite[u][v] for u, v in queries]