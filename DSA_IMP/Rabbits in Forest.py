# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)  # Count occurrences of each answer
        result = 0
        
        for answer, freq in count.items():
            # The group size is answer + 1
            group_size = answer + 1
            # The number of groups needed is the ceiling of freq / group_size
            result += ((freq + group_size - 1) // group_size) * group_size
        
        return result