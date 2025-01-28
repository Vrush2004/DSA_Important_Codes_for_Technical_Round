# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Initialize a pointer for the position of unique elements
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # Check if the current element is unique (or at the beginning)
            if k == 0 or nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Update the position with the unique element
                k += 1  # Move the pointer for unique elements
        
        # Return the number of unique elements
        return k
    

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Pointer for the position to update
        k = 0

        # Iterate through the array
        for num in nums:
            # Allow each number to appear at most twice
            if k < 2 or nums[k - 2] != num:
                nums[k] = num  # Place the current number at the position
                k += 1  # Increment the position pointer

        # Return the number of elements after removing duplicates
        return k
