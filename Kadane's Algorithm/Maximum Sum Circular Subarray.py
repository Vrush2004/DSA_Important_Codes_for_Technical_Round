# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

class Solution:
    def maxSubarraySumCircular(self, nums):
        # Step 1: Find the maximum sum subarray using Kadane's Algorithm
        def kadane(nums):
            currMax = nums[0]
            maxSum = nums[0]

            for i in range(1, len(nums)):
                num = nums[i]
                currMax = max(num, currMax + num)
                maxSum = max(maxSum, currMax)

            return maxSum

        # Step 2: Case 1: The result is the same as the standard maximum subarray sum
        max_sum = kadane(nums)

        # Step 3: Case 2: Find the sum of the entire array and subtract the result of Kadane's on the inverted array
        total_sum = sum(nums)
        inverted_nums = [-num for num in nums]
        inverted_max = kadane(inverted_nums)

        # Step 4: The maximum circular sum is the total sum minus the minimum subarray sum
        max_circular_sum = total_sum + inverted_max

        # Step 5: Return the maximum of normal max sum or circular max sum
        if max_circular_sum == 0:  # To handle edge case when all elements are negative
            return max_sum
        return max(max_sum, max_circular_sum)

# Example usage:
sol = Solution()
print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # Output: 3