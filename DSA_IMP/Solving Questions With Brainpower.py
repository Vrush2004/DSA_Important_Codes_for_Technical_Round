# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# Output: 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # Extra space to avoid out-of-bounds checks

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_index = i + brainpower + 1
            
            # Solve current question and skip brainpower[i] questions
            solve = points + (dp[next_index] if next_index < n else 0)
            
            # Skip the current question
            skip = dp[i + 1]

            # Take the maximum
            dp[i] = max(solve, skip)
        
        return dp[0]