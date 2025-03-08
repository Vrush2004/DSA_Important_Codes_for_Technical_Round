# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        
        # Sliding window approach
        for i in range(len(blocks) - k + 1):
            window = blocks[i:i + k]  # Get the substring of length k
            white_count = window.count('W')  # Count 'W' in the window
            min_operations = min(min_operations, white_count)  # Update min operations
        
        return min_operations