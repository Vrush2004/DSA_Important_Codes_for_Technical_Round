# Input: num = 3749
# Output: "MMMDCCXLIX"
# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral mappings for each decimal place
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = []
        
        # Loop through the Roman numeral mappings
        for value, symbol in roman_numerals:
            # While the number is greater than or equal to the value, append the symbol
            while num >= value:
                result.append(symbol)
                num -= value  # Subtract the value from the number
        
        # Join the list of symbols into a single string and return it
        return ''.join(result)