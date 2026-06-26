class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                row_check = (r,"row",value)
                col_check = (c,"col",value)
                box_check = (r//3,c//3,"box",value)

                if row_check in s or col_check in s or box_check in s:
                    return False 
                s.add(row_check)
                s.add(col_check)
                s.add(box_check)
        
        return True