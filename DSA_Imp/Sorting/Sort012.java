// Given an array containing 0's, 1's and 2's. Sort the array.
// Sample input 
// arr ={0,1,1,0,2,1,0,2,0,2,1}
// Sample output
// arr = {0,0,0,0,1,1,1,1,2,2,2}

package DSA_Imp.Sorting;

public class Sort012 {
    public static void main(String[] args){
        int[] arr = {1,1,0,2,1,0,2,1,0,2,1,0,1};
        sort(arr);
        for (int val : arr){
            System.out.println(val + " ");
        }
    }

    public static void sort(int[] arr){
        int i=0, j=0, k=arr.length-1;
        while(i<=k){
            if(arr[i] == 0){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j++;
            }else if(arr[i] == 1){
                i++;
            }else{
                int temp = arr[i];
                arr[i] = arr[k];
                arr[k] = temp;
                k--;
            }
        }
    }
}
