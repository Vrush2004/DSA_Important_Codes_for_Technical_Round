# Input: nums = [5,2,5,4,5], k = 2
# Output: 2
# Explanation: The operations can be performed in order using valid integers 4 and then 2.

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)