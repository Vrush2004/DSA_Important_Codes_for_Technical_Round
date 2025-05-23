# Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
# Output: 1
# Explanation:
# After removing queries[2], nums can still be converted to a zero array.
# Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
# Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)