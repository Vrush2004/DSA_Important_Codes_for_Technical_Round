# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            # Include nums[index]
            include = dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index]
            exclude = dfs(index + 1, current_xor)
            return include + exclude

        return dfs(0, 0)