package Sorting;
import java.util.Arrays;

class CountingSort {
    void applycountSort(int array[], int size) {
        // Output array
        int[] output = new int[size];
        
        // Find the maximum value in the input array
        int max = array[0];
        for (int i = 1; i < size; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        
        // Create count array
        int[] count = new int[max + 1];
        
        // Initialize count array
        for (int i = 0; i <= max; i++) {  // Corrected to `<= max`
            count[i] = 0;
        }

        // Store the count of each element
        for (int i = 0; i < size; i++) {
            count[array[i]]++;
        }

        // Change count[i] so that it now contains the actual position of this element in output[]
        for (int i = 1; i <= max; i++) {
            count[i] += count[i - 1];
        }

        // Build the output array
        for (int i = size - 1; i >= 0; i--) {
            output[count[array[i]] - 1] = array[i];
            count[array[i]]--;
        }

        // Copy the output array to arr[], so that arr[] now contains sorted numbers
        for (int i = 0; i < size; i++) {
            array[i] = output[i];
        }
    }

    public static void main(String args[]) {
        int[] data = {2, 5, 2, 8, 1, 4, 1};
        int size = data.length;

        CountingSort obj = new CountingSort();
        obj.applycountSort(data, size);

        System.out.println("Array After Sorting: ");
        System.out.println(Arrays.toString(data));
    }
}
