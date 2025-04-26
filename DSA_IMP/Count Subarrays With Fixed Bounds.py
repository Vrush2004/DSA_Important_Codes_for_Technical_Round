# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0  # To store the result
        last_minK = last_maxK = -1  # The last positions of minK and maxK
        last_invalid = -1  # The last invalid position
        
        for i, num in enumerate(nums):
            # If the current number is out of bounds, it invalidates the subarray
            if num < minK or num > maxK:
                last_invalid = i
            
            # If the number is minK, update last_minK
            if num == minK:
                last_minK = i
            
            # If the number is maxK, update last_maxK
            if num == maxK:
                last_maxK = i
            
            # Count valid subarrays if both minK and maxK are within the subarray
            if last_minK != -1 and last_maxK != -1:
                # The valid subarray starts from the position after the last invalid element
                count += max(0, min(last_minK, last_maxK) - last_invalid)
        
        return count
