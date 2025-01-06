// Give an array of integers. Find the maximum subarray sum.
// Sample input 
// arr={2,-3,-2,6,-8,2,1,9,-6,4}
// Sample output
// 13
// Time complexity = O(n)
// space complexity = O(1)

package DSA_Exercise.DynamicProgramming;

public class MaxSubarraySum {
    public static void main(String[] args){
        int[] arr = {2,-3,-2,6,-8,2,1,9,-6,4};
        System.out.println(maxsumsubarr(arr));
    }

    public static int maxsumsubarr(int[] arr){
        int currSum = 0;
        int maxSum = Integer.MIN_VALUE;

        for(int i =0; i<arr.length; i++){
            currSum = Math.max(arr[i], currSum + arr[i]);
            maxSum = Math.max(currSum, maxSum);
        }
        return maxSum;
    }
}