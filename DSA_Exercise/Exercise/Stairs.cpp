// You are climbing a staircase and it takes A steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
// Return the number of distinct ways modulo 1000000007

#define MOD 1000000007

int Solution::climbStairs(int A) {
    // If there are no steps or just one step, there's only one way to climb
    if (A == 0) return 1;
    if (A == 1) return 1;
    
    // Initialize dp array for number of ways
    long long dp[A + 1];
    dp[0] = 1; // Base case: 1 way to stay at the ground
    dp[1] = 1; // Base case: 1 way to reach the first step
    
    // Fill the dp array using the recurrence relation
    for (int i = 2; i <= A; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }
    
    return dp[A];
}