# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value greater than the maximum amount (infinity substitute)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1