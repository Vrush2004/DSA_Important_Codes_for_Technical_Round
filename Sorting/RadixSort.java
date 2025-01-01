package Sorting;
import java.util.Arrays; // Importing library for array utilities

public class RadixSort {

    public static void main(String[] args) {
        int[] a = {92, 106, 365, 90, 33, 19, 72, 56, 45, 12}; // Initializing array
        radixSort(a);

        System.out.println("\nThe sorted list is:");
        for (int num : a) {
            System.out.print(" " + num); // Printing the sorted list
        }
    }

    // Function to find the maximum number in the array
    public static int findMax(int[] a) {
        int max = a[0];
        for (int i = 1; i < a.length; i++) {
            if (a[i] > max) {
                max = a[i];
            }
        }
        return max;
    }

    // Function to perform radix sort
    public static void radixSort(int[] a) {
        int n = a.length;
        int[][] bucket = new int[10][n]; // Buckets for each digit (0-9)
        int[] bucketCount = new int[10]; // To track the count in each bucket
        int divisor = 1;
        int max = findMax(a);

        // Determine the number of passes required (based on max value)
        int numberOfPasses = 0;
        while (max > 0) {
            numberOfPasses++;
            max /= 10;
        }

        // Perform sorting for each digit place
        for (int pass = 0; pass < numberOfPasses; pass++) {
            Arrays.fill(bucketCount, 0); // Reset bucket counts

            // Place numbers into corresponding buckets
            for (int i = 0; i < n; i++) {
                int remainder = (a[i] / divisor) % 10;
                bucket[remainder][bucketCount[remainder]++] = a[i];
            }

            // Collect numbers back into the original array
            int index = 0;
            for (int k = 0; k < 10; k++) {
                for (int j = 0; j < bucketCount[k]; j++) {
                    a[index++] = bucket[k][j];
                }
            }

            divisor *= 10; // Move to the next digit place
        }
    }
}