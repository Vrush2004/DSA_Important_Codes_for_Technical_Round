#include <iostream>
#include <vector>
using namespace std;

bool dfs(int node, vector<vector<int>>& adj, vector<int>& visited, vector<int>& inStack) {
    // Mark the node as visited and add it to the recursion stack
    visited[node] = 1;
    inStack[node] = 1;
    
    // Traverse all neighbors
    for (int neighbor : adj[node]) {
        if (inStack[neighbor]) {
            // If the neighbor is in the recursion stack, cycle is found
            return true;
        }
        if (!visited[neighbor] && dfs(neighbor, adj, visited, inStack)) {
            // If the neighbor is not visited and DFS returns true (cycle detected)
            return true;
        }
    }
    
    // Remove the node from the recursion stack as we are done processing it
    inStack[node] = 0;
    return false;
}

int Solution::solve(int A, vector<vector<int>>& B) {
    // Step 1: Construct the adjacency list
    vector<vector<int>> adj(A + 1);  // Adjacency list (1-indexed)
    for (auto& edge : B) {
        adj[edge[0]].push_back(edge[1]);
    }
    
    // Step 2: Initialize visited and inStack arrays
    vector<int> visited(A + 1, 0);  // 0 = not visited, 1 = visited
    vector<int> inStack(A + 1, 0);  // 0 = not in recursion stack, 1 = in stack
    
    // Step 3: Perform DFS on each unvisited node
    for (int i = 1; i <= A; i++) {
        if (!visited[i]) {
            if (dfs(i, adj, visited, inStack)) {
                return 1;  // Cycle detected
            }
        }
    }
    
    // Step 4: No cycle found
    return 0;
}

int main() {
    // Example 1
    int A1 = 5;
    vector<vector<int>> B1 = { {1, 2}, {4, 1}, {2, 4}, {3, 4}, {5, 2}, {1, 3} };
    Solution sol;
    cout << sol.solve(A1, B1) << endl; // Output: 1

    // Example 2
    int A2 = 5;
    vector<vector<int>> B2 = { {1, 2}, {2, 3}, {3, 4}, {4, 5} };
    cout << sol.solve(A2, B2) << endl; // Output: 0

    return 0;
}