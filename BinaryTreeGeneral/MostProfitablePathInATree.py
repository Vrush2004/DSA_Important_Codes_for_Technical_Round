# Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
# Output: 6
# Explanation: 
# The above diagram represents the given tree. The game goes as follows:
# - Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
#   Alice's net income is now -2.
# - Both Alice and Bob move to node 1. 
#   Since they reach here simultaneously, they open the gate together and share the reward.
#   Alice's net income becomes -2 + (4 / 2) = 0.
# - Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
#   Bob moves on to node 0, and stops moving.
# - Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
# Now, neither Alice nor Bob can make any further moves, and the game ends.
# It is not possible for Alice to get a higher net income.

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = {i: [] for i in range(len(amount))}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = [-1] * len(amount)
        path = []

        def fillBobPath(node, parent):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fillBobPath(neighbor, node):
                        return True
                    path.pop()

        fillBobPath(bob, -1)
        for i, node in enumerate(path):
            bobPath[node] = i
        
        def getAliceMaxScore(node, parent, currScore, timestamp):
            if bobPath[node] == -1 or bobPath[node] > timestamp:
                currScore += amount[node]
            elif bobPath[node] == timestamp:
                currScore += amount[node] // 2
            return currScore if len(graph[node]) == 1 and node != 0 else max(getAliceMaxScore(neighbor, node, currScore, timestamp + 1) for neighbor in graph[node] if neighbor != parent)

        return getAliceMaxScore(0, -1, 0, 0)