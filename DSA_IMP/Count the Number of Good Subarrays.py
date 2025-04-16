# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.

from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count_pairs = 0
        freq_map = defaultdict(int)
        result = 0
        left = 0
        
        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            
            count_pairs += freq_map[nums[right]] - 1
            
            while count_pairs >= k:
                result += len(nums) - right
                freq_map[nums[left]] -= 1
                count_pairs -= freq_map[nums[left]]  
                left += 1
        
        return result