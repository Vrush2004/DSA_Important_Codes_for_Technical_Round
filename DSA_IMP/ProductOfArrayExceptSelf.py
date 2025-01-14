# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Time Complexity: O(n) 
# Space Complexity: O(1) 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate the prefix product for each element
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate the suffix product and multiply with the prefix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer