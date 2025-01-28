# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize variables
        n = len(nums)
        current_sum = 0
        min_length = float('inf')  # Use infinity as a placeholder for the minimum length
        
        left = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            # When the sum meets or exceeds the target, try to shrink the window
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)  # Update the minimal length
                current_sum -= nums[left]  # Shrink the window from the left
                left += 1
        
        # If min_length is still infinity, return 0 (no valid subarray found)
        return min_length if min_length != float('inf') else 0