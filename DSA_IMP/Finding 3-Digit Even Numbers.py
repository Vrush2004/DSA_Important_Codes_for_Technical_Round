# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.

from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        digit_count = Counter(digits)

        for num in range(100, 1000, 2):  # Only even 3-digit numbers
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            temp_count = Counter([d1, d2, d3])
            
            if all(temp_count[d] <= digit_count[d] for d in temp_count):
                result.add(num)

        return sorted(result)