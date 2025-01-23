# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left, right = 0, len(numbers) - 1
        
        # Loop until the pointers meet
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed result
            elif current_sum < target:
                left += 1  # Move left pointer to the right to increase the sum
            else:
                right -= 1  # Move right pointer to the left to decrease the sum