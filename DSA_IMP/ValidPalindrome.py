# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter the string manually to retain only alphanumeric characters
        filtered = []
        for char in s:
            # Check if the character is alphanumeric
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                # Convert uppercase letters to lowercase
                if 'A' <= char <= 'Z':
                    filtered.append(chr(ord(char) + 32))  # Convert to lowercase
                else:
                    filtered.append(char)
        
        # Step 2: Check if the filtered string is a palindrome
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        
        return True