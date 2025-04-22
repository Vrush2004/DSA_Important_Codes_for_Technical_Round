# Input: differences = [1,-3,4], lower = 1, upper = 6
# Output: 2
# Explanation: The possible hidden sequences are:
# - [3, 4, 1, 5]
# - [4, 5, 2, 6]
# Thus, we return 2.

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val, max_val = 0, 0
        curr_val = 0
      
        for diff in differences:
            curr_val += diff
            min_val = min(min_val, curr_val)
            max_val = max(max_val, curr_val)
        
        valid_start_min = lower - min_val
        valid_start_max = upper - max_val
        
        if valid_start_min > valid_start_max:
            return 0
        return valid_start_max - valid_start_min + 1