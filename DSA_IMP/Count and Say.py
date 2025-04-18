# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_sequence = self.countAndSay(n - 1)
        
        result = []
        count = 1
        
        for i in range(1, len(prev_sequence)):
            if prev_sequence[i] == prev_sequence[i - 1]:
                count += 1
            else:
                result.append(str(count) + prev_sequence[i - 1])
                count = 1  
        
        result.append(str(count) + prev_sequence[-1])
        
        return ''.join(result)

sol = Solution()
print(sol.countAndSay(4))  
print(sol.countAndSay(1))  