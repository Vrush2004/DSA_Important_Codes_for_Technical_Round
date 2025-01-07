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