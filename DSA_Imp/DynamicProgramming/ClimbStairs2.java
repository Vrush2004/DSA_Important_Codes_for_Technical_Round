// Give an integer array A of length N. Where A is the cost of stepping on the ith stair.
// From ith stair, you can go to i+1th or i+2th numbered stair. Initially, you are at 1st stair find the minimum cost to reach Nth stair.
// Sample input = arr = {1,2,3,4}
// Sample output = 7
// Time complexity = O(n)
// space complexity = O(n)

package DSA_Imp.DynamicProgramming;

public class ClimbStairs2 {
    public static void main(String[] args){
        int[] arr = {1,2,4,3,6,5,2,7,1};
        System.out.println(stairs(arr, arr.length, new int[arr.length + 1]));
    }
    
    public static int stairs(int[] arr, int n, int[] dp){
        if(n == 1){
            return arr[0];
        }

        if(n == 2){
            return arr[0] + arr[1];
        }

        if(dp[n] != 0){
            return dp[n];
        }
        int f1 = stairs(arr, n-1, dp);
        int f2 = stairs(arr, n-2, dp);
        int ans = Math.min(f1,f2) + arr[n-1];
        dp[n] = ans;
        return ans;
    }
}