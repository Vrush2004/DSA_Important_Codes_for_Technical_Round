# Input
# ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
# Output
# [null, -1, null, null, null, null, 1, null, 2]
# Explanation
# NumberContainers nc = new NumberContainers();
# nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
# nc.change(2, 10); // Your container at index 2 will be filled with number 10.
# nc.change(1, 10); // Your container at index 1 will be filled with number 10.
# nc.change(3, 10); // Your container at index 3 will be filled with number 10.
# nc.change(5, 10); // Your container at index 5 will be filled with number 10.
# nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
# nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
# nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.

import heapq

class NumberContainers:

    def __init__(self):
        self.index_map = {}  # Stores index -> number
        self.number_map = {}  # Stores number -> min-heap of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number != number:
                # Lazy removal: We do NOT remove from heap directly (O(N)), but update `index_map`
                self.index_map[index] = number
                heapq.heappush(self.number_map.setdefault(number, []), index)
        else:
            self.index_map[index] = number
            heapq.heappush(self.number_map.setdefault(number, []), index)

    def find(self, number: int) -> int:
        if number not in self.number_map or not self.number_map[number]:
            return -1
        
        # Remove outdated indices from the heap (Lazy deletion)
        while self.number_map[number]:
            smallest_index = self.number_map[number][0]  # Peek the min index
            if self.index_map.get(smallest_index) == number:
                return smallest_index  # Return the valid smallest index
            heapq.heappop(self.number_map[number])  # Remove outdated index
        
        return -1  # No valid index found