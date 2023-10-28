class Solution:
    def exist(self,board,word):
        m,n=len(board),len(board[0])
        ind=0
        def f(i,j,ind):
            if ind==len(word): return True
            if i<0 or j<0 or i==m or j==n or board[i][j]!=word[ind] or board[i][j]=='#': return False
            c=board[i][j]
            board[i][j]='#'
            ans=f(i+1,j,ind+1) or f(i,j+1,ind+1) or f(i-1,j,ind+1) or f(i,j-1,ind+1)
            board[i][j]=c
            return ans
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[ind]:
                    if f(i,j,ind): return True
        return False