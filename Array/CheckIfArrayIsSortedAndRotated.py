# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Initialize a variable to count decreases
        decrease_count = 0
        n = len(nums)
        
        # Iterate through the array and count how many times there is a decrease
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next element (considering circular array)
                decrease_count += 1
        
        # If there is more than one decrease, return False
        return decrease_count <= 1