// Given two sorted arrays of integers A and B, sorted in ascending order.
// Merge the two arrays A and B into a single array such that it contain all the elements from A and B and it remain sorted at the same time.
// Find and return the resultant merged array.

package DSA_Exercise.Exercise;

public class MergeTwoSortedArrays {
    public int[] solve(int[] A, int[] B) {
        int n = A.length;
        int m = B.length;
        
        // Resultant array to hold the merged result
        int[] result = new int[n + m];
        
        int i = 0, j = 0, k = 0;
        
        // Merge arrays A and B
        while (i < n && j < m) {
            if (A[i] <= B[j]) {
                result[k++] = A[i++];
            } else {
                result[k++] = B[j++];
            }
        }
        
        // If any elements are left in A, add them
        while (i < n) {
            result[k++] = A[i++];
        }
        
        // If any elements are left in B, add them
        while (j < m) {
            result[k++] = B[j++];
        }
        
        return result;
    }
}