# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the potential profit and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        # Iterate through the prices
        for i in range(1, len(prices)):
            # If there is a profit (price increased), add the difference to max_profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit