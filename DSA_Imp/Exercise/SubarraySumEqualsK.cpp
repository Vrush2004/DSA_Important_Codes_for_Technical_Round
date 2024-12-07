#include <vector>
#include <unordered_map>
using namespace std;

int Solution::solve(vector<int> &A, int B) {
    unordered_map<int, int> prefixSumCount;
    int currentPrefixSum = 0;
    int totalCount = 0;

    // Initialize the map with the prefix sum 0 having one count
    prefixSumCount[0] = 1;

    // Iterate through the array
    for (int i = 0; i < A.size(); ++i) {
        // Update the current prefix sum
        currentPrefixSum += A[i];

        // Check if there exists a previous prefix sum such that:
        // currentPrefixSum - previousPrefixSum = B
        if (prefixSumCount.find(currentPrefixSum - B) != prefixSumCount.end()) {
            totalCount += prefixSumCount[currentPrefixSum - B];
        }

        // Update the prefix sum count in the map
        prefixSumCount[currentPrefixSum]++;
    }

    return totalCount;
}
