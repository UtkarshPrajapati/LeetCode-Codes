class Solution:
    def solveSudoku(self, b):
        f=lambda b,row,col,c: not any(b[i][col]==c or b[row][i]==c or b[3*(row//3)+i//3][3*(col//3)+i%3]==c for i in range(9))
        for i in range(9):
            for j in range(9):
                if b[i][j]==".":
                    for c in "123456789":
                        if f(b,i,j,c):
                            b[i][j] = c
                            if self.solveSudoku(b): return True
                            b[i][j] = "."
                    return False
        return True