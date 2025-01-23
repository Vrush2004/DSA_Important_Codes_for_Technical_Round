# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # m is the number of rows, n is the number of columns
        m, n = len(grid), len(grid[0])
        
        # Count the number of servers in each row and each column
        row_count = [0] * m
        col_count = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Now count the servers that can communicate
        server_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # If the server in cell (i, j) can communicate (i.e., it's in a row or column with another server)
                    if row_count[i] > 1 or col_count[j] > 1:
                        server_count += 1
        
        return server_count