package Sorting;

public class HeapSort {

    // Function to heapify a subtree rooted at index i
    public static void heapify(int[] arr, int n, int i) {
        int largest = i; // Initialize the largest as root
        int left = 2 * i + 1; // Left child
        int right = 2 * i + 2; // Right child

        // If left child is larger than root
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        // If right child is larger than the current largest
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        // If root is not the largest
        if (largest != i) {
            // Swap root with the largest
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            
            // Recursively heapify the affected subtree
            heapify(arr, n, largest);
        }
    }

    // Function to perform heap sort
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build the max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extract elements from the heap one by one
        for (int i = n - 1; i > 0; i--) {
            // Move current root to the end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Heapify the reduced heap
            heapify(arr, i, 0);
        }
    }

    // Function to print the array
    public static void display(int[] arr) {
        for (int num : arr) {
            System.out.print(num + "\t");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {1, 14, 3, 7, 0};
        System.out.println("Unsorted array:");
        display(arr);

        heapSort(arr);

        System.out.println("Sorted array:");
        display(arr);
    }
}