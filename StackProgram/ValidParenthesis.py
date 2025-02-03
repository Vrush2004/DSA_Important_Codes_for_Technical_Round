# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop if stack is not empty
                if mapping[char] != top_element:  # Check if it matches the expected open bracket
                    return False
            else:
                stack.append(char)  # Push open brackets onto the stack
        
        return not stack  # Stack should be empty if all brackets are matched