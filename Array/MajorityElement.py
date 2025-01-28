# Input: nums = [3,2,3]
# Output: 3

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize candidate and count
        candidate = None
        count = 0
        
        # First pass: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Second pass (optional): Verify the candidate
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        
        # Should not reach here as majority element is guaranteed
        return -1