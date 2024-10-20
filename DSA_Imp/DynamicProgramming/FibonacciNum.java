// Find nth fibonacci number.
// Fibonacci numbers form a sequence in which every number is the sum of two preceding numbers.
// First few fibonacci numbers are - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
// Sample input N=10
// Sample output = 55
// Time complexity = O(n)
// space complexity = O(n)

package DSA_Imp.DynamicProgramming;

public class FibonacciNum {
    public static void main(String [] args){
        int n = 9;
        System.out.println(fib(n, new int[n+1]));
        System.out.println(fibTab(n));
    }

    public static int fibTab(int n){
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;

        for(int i=2; i<dp.length; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    public static int fib(int n, int[] dp){
        if(n == 0 || n==1){
            return n;
        }

        if(dp[n] != 0){
            return dp[n];
        }

        int fn = fib(n-1, dp) + fib(n-2, dp);
        dp[n] = fn;
        return fn;
    }
}