// Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.
// This matrix A has the following properties:
// Integers in each row are sorted from left to right.
// The first integer of each row is greater than or equal to the last integer of the previous row.
// Return 1 if B is present in A, else return 0.
// NOTE: Rows are numbered from top to bottom, and columns are from left to right.

int Solution::searchMatrix(vector<vector<int>>& A, int B) {
    int N = A.size();    // Number of rows
    int M = A[0].size(); // Number of columns
    
    // Binary search over the entire matrix treated as a 1D array
    int left = 0, right = N * M - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        // Calculate row and column based on mid index
        int row = mid / M;
        int col = mid % M;
        
        if (A[row][col] == B) {
            return 1;  // B is found in the matrix
        } else if (A[row][col] < B) {
            left = mid + 1;  // Search in the right half
        } else {
            right = mid - 1; // Search in the left half
        }
    }
    
    return 0; // B is not found in the matrix
}