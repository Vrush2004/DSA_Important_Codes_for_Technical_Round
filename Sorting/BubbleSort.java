// Time Complexity : O(N^2)
// Space Complexity : O(1)

package Sorting;

class Main
{
    static void BubbleSort(int a[])
    {
        int len = a.length; // calculating the length of array
        for (int i = 0; i < len-1; i++) {

            // for optimization when array is already sorted & no swapping happens
            boolean swapped = false;
            for (int j = 0; j < len - i - 1; j++) 
            { 
                if (a[j] > a[j + 1]) //comparing the pair of elements
                {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                    swapped = true;
                }
            }
            if(swapped == false)
                break;

        }
    }

    static void printArray(int a[])
    {
        int len = a.length;
        for (int i = 0; i < len; i++)
            System.out.print(a[i] + " "); 

        System.out.println();
    }

    public static void main(String args[])
    {
        int arr[] = {4,2,8,1,9,6};

        BubbleSort(arr);

        System.out.println("Sorted array");

        printArray(arr);
    }
}