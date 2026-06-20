class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]
                if value == ".":
                    continue
                r_check = (r,"row",value)
                c_check = (c,"column",value)
                b_check = (r//3,c//3,"box",value)

                if r_check in s or c_check in s or b_check in s:
                    return False

                s.add(r_check)
                s.add(c_check)
                s.add(b_check)
        return True