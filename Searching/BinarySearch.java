import java.util.*;

public class BinarySearch{
    public static void main(String[] args){
        int[] arr = {3,2,1,7,5,6,4};

        // Sorting the Given Array
        Arrays.sort(arr);    
        System.out.print("The Given Array is : ");
        
        // Printing the array using loops
        for(int i = 0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        int len = Arrays.binarySearch(arr,3);    // using binarysearch function
        System.out.println("Element is Found at " + (len+1) + " Position." );
    }
}
// Space Complexity : O(log n)
// Time Complexity : O(log n)