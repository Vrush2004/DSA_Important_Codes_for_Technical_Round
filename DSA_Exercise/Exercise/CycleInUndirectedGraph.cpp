#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    // Traverse all neighbors of the current node
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            // If neighbor is not visited, recursively call DFS
            if (dfs(neighbor, node, adj, visited)) {
                return true;
            }
        }
        // If the neighbor is visited and is not the parent, a cycle is found
        else if (neighbor != parent) {
            return true;
        }
    }
    return false;
}

int Solution::solve(int A, vector<vector<int>>& B) {
    // Step 1: Construct the adjacency list
    vector<vector<int>> adj(A + 1);  // Adjacency list (1-indexed)
    for (auto& edge : B) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }

    // Step 2: Initialize visited array to keep track of visited nodes
    vector<bool> visited(A + 1, false);

    // Step 3: Run DFS on every unvisited node
    for (int i = 1; i <= A; i++) {
        if (!visited[i]) {
            // If DFS detects a cycle, return 1
            if (dfs(i, -1, adj, visited)) {
                return 1;
            }
        }
    }

    // Step 4: No cycle found, return 0
    return 0;
}

int main() {
    // Example 1
    int A1 = 5;
    vector<vector<int>> B1 = { {1, 2}, {1, 3}, {2, 3}, {1, 4}, {4, 5} };
    Solution sol;
    cout << sol.solve(A1, B1) << endl; // Output: 1

    // Example 2
    int A2 = 3;
    vector<vector<int>> B2 = { {1, 2}, {1, 3} };
    cout << sol.solve(A2, B2) << endl; // Output: 0

    return 0;
}