class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking 3*3 Box
        for r in range(0,8,3):
            for c in range(0,8,3):
                box=board[r+0][c:c+3]+board[r+1][c:c+3]+board[r+2][c:c+3]
                emptys_count=box.count('.')
                set_box=set(box)
                if len(set_box)-1!=len(box)-emptys_count:
                    return False

        # checking every horizontal row
        for row in board:
            emptys_count=row.count('.')
            set_row=set(row)
            if len(set_row)-1!=len(row)-emptys_count:
                return False
        
        # checking every vertical column
        for c in range(0,9):
            col_row=[]
            for r in range(0,9):
                col_row.append(board[r][c])
            emptys_count=col_row.count('.')
            set_col_row=set(col_row)
            if len(set_col_row)-1!=len(col_row)-emptys_count:
                return False
        
        return True
