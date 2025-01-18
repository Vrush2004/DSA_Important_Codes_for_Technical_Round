import os
from collections import deque

def bfs(n, m, edges, s):
    # Create an adjacency list to represent the graph
    adj_list = {i: [] for i in range(1, n + 1)}
    
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Initialize the distances array with -1 (unreachable)
    distances = [-1] * (n + 1)
    distances[s] = 0
    
    # Use BFS to calculate the shortest distances
    queue = deque([s])
    
    while queue:
        current_node = queue.popleft()
        
        # Traverse all neighbors of the current node
        for neighbor in adj_list[current_node]:
            if distances[neighbor] == -1:  # If not visited
                distances[neighbor] = distances[current_node] + 6
                queue.append(neighbor)
    
    # We exclude the distance of the start node itself (index 0 is ignored)
    result = [distances[i] for i in range(1, n + 1) if i != s]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()