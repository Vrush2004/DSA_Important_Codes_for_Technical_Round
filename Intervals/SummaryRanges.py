# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]  # Start of the current range

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # Break in the sequence
                if start == nums[i - 1]:
                    result.append(str(start))  # Single number
                else:
                    result.append(f"{start}->{nums[i - 1]}")  # Range
                start = nums[i]  # Start a new range

        # Add the last range after loop
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result