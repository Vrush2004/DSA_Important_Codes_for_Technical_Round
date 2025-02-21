# Input: n = 10
# Output: 182
# Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
# - 1 since 1 * 1 = 1
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
# Hence, the punishment number of 10 is 1 + 81 + 100 = 182

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int, index: int, curr_sum: int) -> bool:
            if index == len(s):
                return curr_sum == target
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if can_partition(s, target, i + 1, curr_sum + num):
                    return True
            return False

        punishment_sum = 0
        for i in range(1, n + 1):
            squared_str = str(i * i)
            if can_partition(squared_str, i, 0, 0):
                punishment_sum += i * i

        return punishment_sum