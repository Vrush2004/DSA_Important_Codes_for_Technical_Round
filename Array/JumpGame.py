# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Variable to track the farthest index we can reach
        farthest = 0
        for i in range(len(nums)):
            # If the current index is not reachable, return False
            if i > farthest:
                return False
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        return False


# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # If there's only one element, no jumps are needed
        if n == 1:
            return 0
        
        # Initialize variables
        jumps = 0  # Number of jumps taken
        current_end = 0  # The farthest index reachable with the current number of jumps
        farthest = 0  # The farthest index reachable overall

        for i in range(n - 1):  # Traverse the array, excluding the last index
            # Update the farthest index reachable
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest  # Update the range for the next jump
                
                # If the farthest index is beyond or at the last index, return jumps
                if current_end >= n - 1:
                    return jumps
        
        return jumps