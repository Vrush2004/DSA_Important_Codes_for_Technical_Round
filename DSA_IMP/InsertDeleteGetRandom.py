# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

import random

class RandomizedSet:

    def __init__(self):
        self.values = []  # List to store the elements
        self.index_map = {}  # Dictionary to store element -> index mapping

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False  # Element already exists, return False
        
        # Add the value to the list and update the index map
        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False  # Element doesn't exist, return False
        
        # Find the index of the value to remove
        index = self.index_map[val]
        last_element = self.values[-1]
        
        # Move the last element to the place of the element to remove
        self.values[index] = last_element
        self.index_map[last_element] = index
        
        # Remove the last element
        self.values.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        # Randomly select an element from the list
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()