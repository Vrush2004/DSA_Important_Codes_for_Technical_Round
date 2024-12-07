/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <queue>
#include <vector>
using namespace std;

/**
 * Perform level order traversal of the binary tree.
 * @input root : The root node of the binary tree.
 * @output Return a 2D integer array denoting the level order traversal.
 */
vector<vector<int>> Solution::solve(TreeNode* root) {
    vector<vector<int>> result;
    
    if (root == NULL) {
        return result;
    }
    
    // Queue for level order traversal
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();  // Number of nodes at the current level
        vector<int> currentLevel;
        
        // Process all nodes at the current level
        for (int i = 0; i < levelSize; i++) {
            TreeNode* currentNode = q.front();
            q.pop();
            currentLevel.push_back(currentNode->val);
            
            // Enqueue the left and right children of the current node
            if (currentNode->left != NULL) {
                q.push(currentNode->left);
            }
            if (currentNode->right != NULL) {
                q.push(currentNode->right);
            }
        }
        
        // Add the current level to the result
        result.push_back(currentLevel);
    }
    
    return result;
}