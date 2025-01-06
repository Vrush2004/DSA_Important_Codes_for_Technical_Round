#include <unordered_set>
#include <algorithm>

int longestConsecutive(const int* A, int n1) {
    // Step 1: Insert all elements into a set for O(1) lookup
    std::unordered_set<int> elements(A, A + n1);

    int longest = 0;

    // Step 2: Iterate over each element in the array
    for (int i = 0; i < n1; ++i) {
        // If the previous element (A[i] - 1) is not in the set, A[i] is the start of a new sequence
        if (elements.find(A[i] - 1) == elements.end()) {
            int current_num = A[i];
            int current_length = 1;

            // Count the length of the consecutive sequence starting from current_num
            while (elements.find(current_num + 1) != elements.end()) {
                current_num++;
                current_length++;
            }

            // Update the longest sequence length
            longest = std::max(longest, current_length);
        }
    }

    return longest;
}
