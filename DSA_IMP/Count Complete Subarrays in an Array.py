# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums):
        total_unique = len(set(nums))  # total distinct elements in the whole array
        count = 0
        n = len(nums)

        for i in range(n):
            freq = defaultdict(int)
            unique = 0
            for j in range(i, n):
                if freq[nums[j]] == 0:
                    unique += 1
                freq[nums[j]] += 1
                if unique == total_unique:
                    count += 1
        return count