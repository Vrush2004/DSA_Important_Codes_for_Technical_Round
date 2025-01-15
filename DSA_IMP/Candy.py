# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # Initialize candies array where every child gets at least one candy
        candies = [1] * n
        
        # Left to right pass: ensure each child has more candies than the left neighbor if rating is higher
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass: ensure each child has more candies than the right neighbor if rating is higher
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the sum of all candies
        return sum(candies)