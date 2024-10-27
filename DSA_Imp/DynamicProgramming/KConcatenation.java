// Give an array of integers(A) and integer K. Another array(B) is formed by concatenating K copies of given array.
// For eg. A= {1,2} and k=3 then, B={1,2,1,2,1,2}
// Find the maximum subarray sum in B.
// Sample input 
// A={-1,4,3,-2}, k=3
// Sample output
// 15
// Time complexity = O(n*k)
// space complexity = O(n*k)

package DSA_Imp.DynamicProgramming;

public class KConcatenation {
    public static void main(String[] args){
        int[] arr = {1,-4, -3, 2};
        System.out.println(maxSum(arr, 3));
    }

    public static int main(int[] arr, int k){

    }

    public static int kadanes(int[] arr){
        int currSum =0;
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i< arr.length; i++){
            currSum = Math.max(currSum+arr[i], arr[i]);
            maxSum = Math.max(maxSum, currSum)
        }
        return maxSum;
    }
}