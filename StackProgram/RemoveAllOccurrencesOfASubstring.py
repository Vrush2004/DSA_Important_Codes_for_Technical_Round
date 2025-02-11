# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)  # Add character to stack
            
            # Check if the last `len(part)` characters match `part`
            if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
                for _ in range(part_length):  # Remove `part` from stack
                    stack.pop()
        
        return "".join(stack)  # Convert stack back to string