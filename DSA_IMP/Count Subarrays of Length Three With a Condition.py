# Input: nums = [1,2,1,4,1]
# Output: 1
# Explanation:
# Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            first = nums[i]
            second = nums[i + 1]
            third = nums[i + 2]
            if first + third == second / 2:
                count += 1
        return count