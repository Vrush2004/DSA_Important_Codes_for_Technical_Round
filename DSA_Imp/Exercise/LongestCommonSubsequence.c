// Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.
// You need to return the length of such longest common subsequence.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int solve(char* A, char* B) {
    int m = strlen(A);
    int n = strlen(B);

    // dp[i][j] will store the length of LCS of A[0..i-1] and B[0..j-1]
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    // Build the dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (A[i - 1] == B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1; // If characters match
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); // If characters don't match
            }
        }
    }

    // The length of the LCS is found at dp[m][n]
    return dp[m][n];
}