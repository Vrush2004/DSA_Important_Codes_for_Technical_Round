# Input: s = "cb34"
# Output: ""
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                # Remove the closest non-digit character to the left (if any)
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

# Example usage:
sol = Solution()
print(sol.clearDigits("abc"))  # Output: "abc"
print(sol.clearDigits("cb34"))  # Output: ""