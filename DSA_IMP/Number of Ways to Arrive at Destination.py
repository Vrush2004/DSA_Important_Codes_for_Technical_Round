# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
# Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
# The four ways to get there in 7 minutes are:
# - 0 ➝ 6
# - 0 ➝ 4 ➝ 6
# - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
# - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

from heapq import heappush, heappop
from collections import defaultdict
from typing import List

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Construct the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))  # Bi-directional road
        
        # Step 2: Initialize Dijkstra's algorithm
        min_heap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        ways = [0] * n
        ways[0] = 1  # 1 way to reach the start
        
        while min_heap:
            curr_time, node = heappop(min_heap)
            
            # If we already found a shorter way, skip processing
            if curr_time > shortest_time[node]:
                continue
            
            for neighbor, travel_time in graph[node]:
                new_time = curr_time + travel_time
                
                # If we find a shorter time to reach neighbor
                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(min_heap, (new_time, neighbor))
                
                # If we find another way with the same shortest time
                elif new_time == shortest_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]