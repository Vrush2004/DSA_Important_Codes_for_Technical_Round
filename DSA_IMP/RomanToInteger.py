# Input: s = "III"
# Output: 3
# Explanation: III = 3
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary for Roman numeral values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the Roman numeral string in reverse
        for char in reversed(s):
            current_value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                # Otherwise, add it to the total
                total += current_value
            
            # Update the previous value for the next iteration
            prev_value = current_value
        
        return total