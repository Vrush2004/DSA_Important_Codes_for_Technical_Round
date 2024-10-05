package Sorting;

// Time Complexity : O(N^2)
// Space Complexity : O(1)
// Best Case : When already Sorted, Worst Case : When reverse Sorted
class Main
{
    public static void main(String args[])
    {
        int a[] = {11, 9, 7, 15, 6, 10, 5, 17};

        System.out.println("Array Before Insertion Sort: ");
        printArray(a);

        InsertionSort(a);

        System.out.println("Array After Insertion Sort: ");
        printArray(a);
    }

    /*Function to sort array using insertion sort*/
    static void InsertionSort(int arr[])
    {
        int len = arr.length;
        for (int i = 1; i < len; i++) 
        { 
            int key = arr[i]; 
            int j = i - 1; 

            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    /* A utility function to print array of size n*/
    static void printArray(int a[])
    {
        int len = a.length;
        for (int i = 0; i < len; ++i)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}