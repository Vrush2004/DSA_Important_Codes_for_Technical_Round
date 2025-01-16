# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
# Explanation:
# A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
# The bitwise XOR of all these numbers is 13, so we return 13.

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # XOR all elements in nums1
        xor1 = 0
        for num in nums1:
            xor1 ^= num
        
        # XOR all elements in nums2
        xor2 = 0
        for num in nums2:
            xor2 ^= num
        
        # If length of nums2 is odd, xor1 contributes to the result
        # If length of nums1 is odd, xor2 contributes to the result
        result = 0
        if len(nums2) % 2 == 1:
            result ^= xor1
        if len(nums1) % 2 == 1:
            result ^= xor2
        
        return result