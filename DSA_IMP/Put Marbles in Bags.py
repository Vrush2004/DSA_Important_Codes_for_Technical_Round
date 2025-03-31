# Input: weights = [1,3,5,1], k = 2
# Output: 4
# Explanation: 
# The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
# The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
# Thus, we return their difference 10 - 6 = 4.

from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0  # Only one bag, so no difference

        # Step 1: Compute adjacent pair sums
        pair_sums = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        
        # Step 2: Sort pair sums
        pair_sums.sort()
        
        # Step 3: Compute max and min sum
        max_score = sum(pair_sums[-(k-1):])  # Largest k-1 elements
        min_score = sum(pair_sums[:k-1])    # Smallest k-1 elements
        
        return max_score - min_score