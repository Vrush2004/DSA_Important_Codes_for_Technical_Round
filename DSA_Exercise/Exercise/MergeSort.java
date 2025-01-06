// Given an integer array A, sort the array using Merge Sort.

package DSA_Exercise.Exercise;

public class MergeSort {
    public int[] solve(int[] A) {
        // If the array is empty or has only one element, return it as is
        if (A == null || A.length <= 1) {
            return A;
        }
        
        // Call the mergeSort helper function
        return mergeSort(A);
    }
    
    // Merge Sort Helper Function
    private int[] mergeSort(int[] A) {
        if (A.length <= 1) {
            return A;
        }
        
        // Divide the array into two halves
        int mid = A.length / 2;
        int[] left = new int[mid];
        int[] right = new int[A.length - mid];
        
        System.arraycopy(A, 0, left, 0, mid);
        System.arraycopy(A, mid, right, 0, A.length - mid);
        
        // Recursively sort both halves
        left = mergeSort(left);
        right = mergeSort(right);
        
        // Merge the sorted halves
        return merge(left, right);
    }
    
    // Merge Helper Function
    private int[] merge(int[] left, int[] right) {
        int[] merged = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        
        // Merge the arrays by comparing elements
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                merged[k++] = left[i++];
            } else {
                merged[k++] = right[j++];
            }
        }
        
        // If there are any remaining elements in left
        while (i < left.length) {
            merged[k++] = left[i++];
        }
        
        // If there are any remaining elements in right
        while (j < right.length) {
            merged[k++] = right[j++];
        }
        
        return merged;
    }
}