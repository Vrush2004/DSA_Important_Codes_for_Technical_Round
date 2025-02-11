# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that end before newInterval starts (No overlap)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Update start
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Update end
            i += 1
        
        # Add the merged interval
        result.append(newInterval)

        # Add remaining intervals (No overlap with newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result