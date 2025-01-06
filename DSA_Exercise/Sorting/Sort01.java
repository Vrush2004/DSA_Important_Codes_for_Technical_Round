// You are given an array of of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.
// Sample input 
// arr ={0,1,1,0,0,1,0,1,0}
// Sample output
// arr = {0,0,0,0,1,1,1,1}

package DSA_Exercise.Sorting;

public class Sort01 {
    public static void main(String[] args){
        int[] arr = {1,1,0,0,1,0,0,1,1,0,0};
        sort(arr);
        for(int val:arr){
            System.out.print(val+ " ");
        }
    }

    public static void sort(int[] arr){
        int i = 0,j=0;
        while(i<arr.length){
            if(arr[i] == 0){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j++;
            }else{
                i++;
            }
        }
    }
}