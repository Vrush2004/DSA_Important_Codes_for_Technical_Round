# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':  # Skip empty cells
                    continue
                
                # Determine the index of the sub-box
                box_index = (i // 3) * 3 + (j // 3)

                # Check if the number is already present in the corresponding row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                # Add the number to the respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        return True