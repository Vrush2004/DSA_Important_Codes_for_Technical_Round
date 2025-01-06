// Given a sorted array of unique elements. Find the minimum element in the array.
// Sample input
// arr ={7, 8, 10, 15, 16, 2, 4, 6}
// Sample output = 2
// time complexity = 0(log2 n)
// space complexity = 0(1)

package DSA_Exercise.BinarySearch;

public class MinInSortedAndRotatedArr {
    public static void main(String[] args){
        int[] arr = {14, 15,20, 22, 3, 5, 7, 9, 11};
        System.out.println(findMin(arr));
    }

    public static int findMin(int[] arr){
        int left = 0, right = arr.length-1;
        while(left < right){
            int mid = (left + right) / 2;
            if(arr[mid] <= arr[right]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return arr[left];
    }
}