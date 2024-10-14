// Give a sorted array and a target. you need to find the first and last position of that target in the array.
// Sample input 
// N=10
// arr={2,3,3,4,5,5,5,5,8}
// target = 5
// sample output = 4 8

package DSA_Imp.BinarySearch;

public class FirstLastIndex {
    public static void main(String[] args){
        int[]arr = {1,2,2,3,3,3,4,4,4,4,4,8};
        
        position(arr,4);
    }
    public static void position(int[]arr, int target){
        int left = 0 ; 
        int right=arr.length-1;
        int first = -1;

        while (left<=right) {
            int mid = (left+right) / 2;
            if (arr[mid]==target){
                first = mid;
                right = mid-1;
            }else if(arr[mid] < target){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }

        left = 0 ; 
        right=arr.length-1;
        int last = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == target){
                last = mid;
                left = mid + 1;
            }else if(arr[mid] < target){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        System.out.println(first + " " + last);
    }
}