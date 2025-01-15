# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
# Time Complexity: O(32)=O(1)
# Space Complexity: O(1)

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits (1's) in num2
        set_bits_num2 = bin(num2).count('1')
        
        # Resultant number x
        x = 0

        # Set bits in x to minimize XOR with num1
        # Traverse through bits of num1 from the most significant to the least significant
        for i in range(31, -1, -1):
            if set_bits_num2 > 0 and (num1 & (1 << i)) != 0:
                x |= (1 << i)
                set_bits_num2 -= 1
        
        # If there are still bits left to be set in x
        for i in range(32):
            if set_bits_num2 == 0:
                break
            if (x & (1 << i)) == 0:
                x |= (1 << i)
                set_bits_num2 -= 1
        
        return x