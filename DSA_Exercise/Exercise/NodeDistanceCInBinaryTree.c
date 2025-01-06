#include <queue>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef struct TreeNode treenode;

// Helper function to find the path from root to node B
bool findPathToNode(treenode* root, int B, vector<treenode*>& path) {
    if (root == NULL) return false;
    path.push_back(root);
    
    if (root->val == B) return true;
    
    if (findPathToNode(root->left, B, path) || findPathToNode(root->right, B, path)) {
        return true;
    }
    
    path.pop_back();  // Backtrack if node B is not found
    return false;
}

// Function to perform BFS to find nodes at distance 'C' from a given node
vector<int> bfsAtDistance(treenode* root, int C) {
    vector<int> result;
    if (root == NULL) return result;
    
    queue<pair<treenode*, int>> q;  // Pair of node and its current distance from root
    q.push({root, 0});
    
    while (!q.empty()) {
        auto [node, dist] = q.front();
        q.pop();
        
        if (dist == C) {
            result.push_back(node->val);
        } else if (dist < C) {
            if (node->left) q.push({node->left, dist + 1});
            if (node->right) q.push({node->right, dist + 1});
        }
    }
    
    return result;
}

// Function to solve the problem
int* solve(treenode* A, int B, int C, int* len1) {
    // Step 1: Find the path from root to node B
    vector<treenode*> path;
    findPathToNode(A, B, path);
    
    // Step 2: Collect nodes at distance C from the node B's descendants
    vector<int> result;
    vector<int> descendants = bfsAtDistance(path.back(), C);  // BFS from node B
    result.insert(result.end(), descendants.begin(), descendants.end());
    
    // Step 3: Collect nodes at distance C from ancestors of B
    for (int i = path.size() - 2; i >= 0; --i) {  // Start from parent of B (ancestors)
        treenode* ancestor = path[i];
        
        // Perform BFS from ancestor excluding the path leading to the parent (avoid going back to B)
        queue<pair<treenode*, int>> q;
        if (ancestor->left != path[i + 1]) q.push({ancestor->left, 1});
        if (ancestor->right != path[i + 1]) q.push({ancestor->right, 1});
        
        // Perform BFS
        while (!q.empty()) {
            auto [node, dist] = q.front();
            q.pop();
            
            if (dist == C) {
                result.push_back(node->val);
            } else if (dist < C) {
                if (node->left) q.push({node->left, dist + 1});
                if (node->right) q.push({node->right, dist + 1});
            }
        }
    }
    
    // Step 4: Prepare output
    *len1 = result.size();
    int* resArray = (int*)malloc(*len1 * sizeof(int));
    for (int i = 0; i < *len1; ++i) {
        resArray[i] = result[i];
    }
    
    return resArray;
}