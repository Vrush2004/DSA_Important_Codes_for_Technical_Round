from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        result = [0] * size
        used = set()

        def backtrack(index):
            if index == size:
                return True  # Successfully filled

            if result[index] != 0:  
                return backtrack(index + 1)  # Skip filled position

            for num in range(n, 0, -1):  # Try larger numbers first
                if num in used:
                    continue

                if num == 1:  
                    result[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used.remove(1)
                else:
                    second_index = index + num
                    if second_index < size and result[second_index] == 0:
                        result[index] = result[second_index] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        result[index] = result[second_index] = 0
                        used.remove(num)

            return False  

        backtrack(0)
        return result