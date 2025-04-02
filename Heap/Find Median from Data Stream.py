# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 
import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (inverted to use min-heap structure in Python)
        self.max_heap = []  # To store the smaller half
        # Min-heap
        self.min_heap = []  # To store the larger half

    def addNum(self, num: int) -> None:
        # Step 1: Add to the max heap
        heapq.heappush(self.max_heap, -num)  # We negate the number to simulate a max-heap
        
        # Step 2: Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move the largest element from max_heap to min_heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if self.min_heap and self.max_heap and (-self.max_heap[0] > self.min_heap[0]):
            # Swap elements if max_heap's root is greater than min_heap's root
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # Step 3: Calculate the median
        if len(self.max_heap) > len(self.min_heap):
            # If max_heap has more elements, the median is the root of max_heap
            return -self.max_heap[0]
        else:
            # If both heaps are of equal size, the median is the average of the roots
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0