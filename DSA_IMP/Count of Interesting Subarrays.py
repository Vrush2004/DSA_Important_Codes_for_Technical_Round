# Input: nums = [3,2,4], modulo = 2, k = 1
# Output: 3
# Explanation: In this example the interesting subarrays are: 
# The subarray nums[0..0] which is [3]. 
# - There is only one index, i = 0, in the range [0, 0] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k.  
# The subarray nums[0..1] which is [3,2].
# - There is only one index, i = 0, in the range [0, 1] that satisfies nums[i] % modulo == k.  
# - Hence, cnt = 1 and cnt % modulo == k.
# The subarray nums[0..2] which is [3,2,4]. 
# - There is only one index, i = 0, in the range [0, 2] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k. 
# It can be shown that there are no other interesting subarrays. So, the answer is 3.

from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        interesting_subarrays = 0
        prefix = 0
        
        for num in nums:
            if num % modulo == k:
                prefix += 1
            
            mod_val = prefix % modulo
            target_val = (mod_val - k + modulo) % modulo
            
            interesting_subarrays += prefix_count[target_val]
            
            prefix_count[mod_val] += 1
        
        return interesting_subarrays