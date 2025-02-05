# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10  # Get the last digit
                total += digit ** 2  # Square the digit and add to total
                num //= 10  # Remove the last digit
            return total

        seen = set()  # Set to track numbers we've seen before
        
        while n != 1 and n not in seen:
            seen.add(n)  # Mark current number as seen
            n = get_next(n)  # Get the next number in the sequence

        return n == 1  # If we reach 1, return True; otherwise, False