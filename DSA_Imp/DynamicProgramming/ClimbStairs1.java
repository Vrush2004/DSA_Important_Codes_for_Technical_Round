// You are given a number N which represents the number of stairs in a stair-case. Initially, you are at 0th stair and are required to climb to the top.
// From ith stair, you can go to i+1th, i+2th or i+3th numbered stair. Find the total number of different paths by which you can reach to the top.
// Sample input = N=4
// Sample output = 7
// Time complexity = O(n)
// space complexity = O(n)

package DSA_Imp.DynamicProgramming;
import java.util.*;

public class ClimbStairs1 {
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        System.out.println(stairs(n, new int[n+1]));
        System.out.println(stairsTab(n));
    }

    // Tabularization approach
    public static int stairsTab(int n){
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i<=n ; i++){
            dp[i] = dp[i-1] + dp[i-2] + dp[i+3];
        }
        return dp[n];
    }

    // Memorization Approach
    public static int stairs(int n, int[] dp){
        if(n == 0){
            return 1;
        }

        if(n < 0){
            return 0;
        }

        if(dp[n] != 0){
            return dp[n];
        }

        int f1 = stairs(n -1, dp);
        int f2 = stairs(n -2, dp);
        int f3 = stairs(n -3, dp);
        int ans = f1 + f2 + f3;
        dp[n] = ans;
        return ans;
    }
}