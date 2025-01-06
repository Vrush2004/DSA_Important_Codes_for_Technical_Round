// Given an array.Find the length of longest strictly increasing subsequence.
// Sample Input 
// arr = {10,2,9,5,7,3,60,80,1}
// Sample output = 5
// Time complexity = O(n^2)
// space complexity = O(n)

package DSA_Exercise.DynamicProgramming;

public class LongestIncSubsequence {
    public static void main(String[] args){
        int[] arr = {10, 2,9,5,7,3,60,80,1};
        // int[] arr = {5,4,3,2,1};
        System.out.println(lis(arr, 0, -1, new int[arr.length][arr.length]));
        int ans = 0;
        for (int i=0; i<arr.length; i++){
            int len = lis2(arr, i);
            ans = Math.max(ans, len);
        }
        System.out.println(ans);
        System.out.println(lisTab(arr));
    }

    // Memorization
    public static int lis2(int[] arr, int i){
        int max= 0;
        for (int j = 0; j<i; j++){
            if(arr[j] < arr[i]){
                max = Math.max(max, lis2(arr,j));
            }
        }
        return max +1;
    }

    // Tabulation
    public static int lisTab(int[] arr){
        int[] dp = new int[arr.length];
        dp[0] = 1;
        int ans = 0;

        for(int i=1; i<arr.length; i++){
            int max =0;
            for(int j =0; j<i; j++){
                if(arr[j] < arr[i]){
                    max = Math.max(max, dp[j]);
                }
            }
            dp[i] = max + 1;
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }

    public static int lis(int[] arr, int idx, int psidx, int[][] dp){
        if(idx == arr.length){
            return 0;
        }

        if(psidx != -1 && dp[idx][psidx] != 0){
            return dp[idx][psidx];
        } 

        int f1 = 0 + lis(arr, idx+1, psidx, dp);
        int f2 = 0;
        if(psidx == -1 || arr[idx] > arr[psidx]){
            f2 = 1+lis(arr, idx+1, idx, dp);
        }
        int ans = Math.max(f1,f2);
        if(psidx != -1){
            dp[idx][psidx] = ans;
        } 
        return ans;
    }
}
