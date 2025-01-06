// Given a sorted rotated array of unique elements and a target. Find the index of target in the array. If target is not present in the array, return -1.
// Sample input 
// arr = {9, 11, 14, 15, 20, 22, 25, 1, 3, 5, 7}
// target = 14
// Sample output = 2
// time complexity = 0(log2 n)
// space complexity = 0(1)

package DSA_Exercise.BinarySearch;

import java.util.Scanner;

public class SearchSortedAndRotatedArray {
    public static void main(String[] args){
        int[] arr = {9, 11, 14, 15, 20, 22, 25, 1, 3, 5, 7};
        Scanner scn = new Scanner(System.in);
        int target = scn.nextInt();
        int minidx = findMin(arr);
        int ans = binarySearch(arr, 0, minidx -1 , target);
        if (ans == -1){
            ans = binarySearch(arr, minidx, arr.length - 1, target);
        }
        System.out.println(ans);
    }

    public static int binarySearch(int[] arr, int left, int right, int target){
        while(left <= right){
            int mid = (left + right) / 2;
            if(arr[mid] == target){
                return mid;
            }else if(arr[mid] < target){
                left = mid + 1;
            }else{
                right = mid -1;
            }
        }
        return -1;
    }

    public static int findMin(int[] arr){
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if(arr[mid] < arr[right]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}
