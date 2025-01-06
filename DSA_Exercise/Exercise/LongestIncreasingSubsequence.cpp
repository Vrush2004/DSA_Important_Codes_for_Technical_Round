// Find the longest increasing subsequence of a given array of integers, A.
// In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.
// In this case, return the length of the longest increasing subsequence.

#include <vector>
#include <algorithm>
using namespace std;

int Solution::lis(const vector<int> &A) {
    int n = A.size();
    
    // dp[i] will store the length of the longest increasing subsequence ending at index i
    vector<int> dp(n, 1);  // Every element can at least form a subsequence of length 1

    // Build the dp array
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (A[j] < A[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    // The result is the maximum value in dp
    return *max_element(dp.begin(), dp.end());
}