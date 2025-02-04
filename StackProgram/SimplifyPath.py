# Input: path = "/home/"
# Output: "/home"
# Explanation:The trailing slash should be removed.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split("/")  # Split path by "/"

        for part in components:
            if part == "..":  # Go to parent directory
                if stack:
                    stack.pop()
            elif part and part != ".":  # Ignore empty and current dir '.'
                stack.append(part)

        return "/" + "/".join(stack)  # Construct simplified path