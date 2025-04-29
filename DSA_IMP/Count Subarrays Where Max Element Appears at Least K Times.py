# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # To keep track of valid subarrays
        result = 0
        
        # Sliding window pointers
        left = 0
        
        # Frequency of the current max element
        freq_max = 0
        max_element = -float('inf')
        
        # Traverse the array with the right pointer
        for right in range(len(nums)):
            # Update the frequency and the max element in the current window
            if nums[right] > max_element:
                max_element = nums[right]
                freq_max = 1
            elif nums[right] == max_element:
                freq_max += 1
            
            # If the frequency of the max element is >= k, count subarrays
            while freq_max >= k:
                result += len(nums) - right
                # Shrink the window from the left
                if nums[left] == max_element:
                    freq_max -= 1
                left += 1
        
        return result
