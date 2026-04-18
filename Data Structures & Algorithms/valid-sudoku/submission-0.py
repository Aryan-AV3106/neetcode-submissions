class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue

                r_check = (r,"row",val)
                c_check =(c,"col",val)
                b_check = (r//3,c//3,"box",val)

                if r_check in s or c_check in s or b_check in s:
                    return False
                
                s.add(r_check)
                s.add(c_check)
                s.add(b_check)
        
        return True