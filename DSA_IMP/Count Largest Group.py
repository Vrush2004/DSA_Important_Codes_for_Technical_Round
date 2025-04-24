# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        groups = defaultdict(int)
        
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] += 1
        
        max_size = max(groups.values())
        return sum(1 for count in groups.values() if count == max_size)