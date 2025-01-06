// Given a sorted array of integers A of size N and an integer B, where array A is rotated at some pivot unknown beforehand.
// For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].
// Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.
// You can assume that no duplicates exist in the array.
// NOTE: You are expected to solve this problem with a time complexity of O(log(N)).

int Solution::search(const vector<int> &A, int B) {
    int left = 0, right = A.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // Check if the target is found
        if (A[mid] == B) {
            return mid;
        }
        
        // Check if the left half is sorted
        if (A[left] <= A[mid]) {
            // If the target is within the left half
            if (A[left] <= B && B < A[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // If the right half is sorted
        else {
            // If the target is within the right half
            if (A[mid] < B && B <= A[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    
    // If the target is not found
    return -1;
}