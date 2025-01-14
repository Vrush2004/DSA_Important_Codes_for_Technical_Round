# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = set()
        C = []
        common_count = 0

        for i in range(n):
            # Add the current elements of A and B to the seen set
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
            
            # Append the count of common elements so far
            C.append(common_count)
        
        return C