# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Initialize prefix_max and suffix_max arrays
        prefix_max = [0] * n
        suffix_max = [0] * n
        
        # Fill prefix_max array with the largest element up to index i
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        # Fill suffix_max array with the largest element from index i to the end
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        # Now check the maximum value for each triplet
        max_value = 0  # If no valid triplet, return 0
        
        for j in range(1, n - 1):  # j is the middle element, can't be the first or last
            i, k = prefix_max[j - 1], suffix_max[j + 1]
            value = (i - nums[j]) * k
            max_value = max(max_value, value)
        
        return max_value

# Example Usage
solution = Solution()
print(solution.maximumTripletValue([12,6,1,2,7]))  # Output: 77
print(solution.maximumTripletValue([1,10,3,4,19]))  # Output: 133
print(solution.maximumTripletValue([1,2,3]))  # Output: 0