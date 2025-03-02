# Input: pattern = "IIIDIDDD"
# Output: "123549876"
# Explanation:
# At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
# At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
# Some possible values of num are "245639871", "135749862", and "123849765".
# It can be proven that "123549876" is the smallest possible num that meets the conditions.
# Note that "123414321" is not possible because the digit '1' is used more than once.

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1 

        for char in pattern + 'I':  
            stack.append(str(num))
            num += 1

            if char == 'I':
                while stack:
                    result.append(stack.pop())

        return ''.join(result)