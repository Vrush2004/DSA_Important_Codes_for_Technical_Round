class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if there's only one row or if numRows is greater than or equal to the length of s
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold each row's characters
        rows = [''] * numRows
        
        # Initialize variables to track the current row and direction
        current_row = 0
        going_down = False
        
        # Traverse the string and place characters in the rows
        for char in s:
            rows[current_row] += char
            # If we reach the top or bottom row, we change the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down based on the direction
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)