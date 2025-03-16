# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation: 
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars  # Binary search range
        
        def canRepairInTime(mid):
            total_cars = sum(math.isqrt(mid // r) for r in ranks)
            return total_cars >= cars
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time
        
        return left