# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]  # Start with the first interval

        # Step 2: Merge intervals
        for i in range(1, len(intervals)):
            prev = merged[-1]  # Last added interval
            curr = intervals[i]

            if curr[0] <= prev[1]:  # Overlapping case
                prev[1] = max(prev[1], curr[1])  # Merge by extending end time
            else:
                merged.append(curr)  # No overlap, add new interval

        return merged