class Solution:
    def exist(self,board,word):
        m,n=len(board),len(board[0])
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        def f(i,j,ind):
            if ind == len(word): return True
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[ind] or board[i][j] == '#': return False
            c, board[i][j] = board[i][j], '#'
            if any(f(i + dx, j + dy, ind + 1) for dx, dy in d): return True
            board[i][j] = c
            return False
        return any(f(i, j, 0) for i in range(m) for j in range(n) if board[i][j] == word[0])