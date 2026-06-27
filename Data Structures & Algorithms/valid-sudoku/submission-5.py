class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s= set()
        for i in range(len(board)):
            for j in range(len(board)):
                value = board[i][j]

                if value == ".":
                    continue 
                
                check_row = (value,"row",i)
                check_col = (value,"col",j)
                check_box = (value,"box",i//3,j//3)

                if check_row in s or check_col in s or check_box in s:
                    return False
                s.add(check_row)
                s.add(check_col)
                s.add(check_box)



        return True