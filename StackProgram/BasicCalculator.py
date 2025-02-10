# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0  # Final result

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Handle multi-digit numbers
            elif char in "+-":
                result += sign * num  # Apply the previous sign
                num = 0  # Reset number
                sign = 1 if char == "+" else -1  # Update sign
            elif char == "(":
                stack.append(result)  # Store result so far
                stack.append(sign)  # Store current sign
                result = 0  # Reset result for sub-expression
                sign = 1  # Reset sign
            elif char == ")":
                result += sign * num  # Add last number
                num = 0
                result *= stack.pop()  # Apply sign before parenthesis
                result += stack.pop()  # Add result before parenthesis
        
        return result + sign * num  # Include last number in the result

# Example usage:
sol = Solution()
print(sol.calculate("1 + 1"))  # Output: 2
print(sol.calculate("2-1 + 2"))  # Output: 3
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23