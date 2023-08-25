class Solution:
    def gameOfLife(self,b):
        m,n=len(b),len(b[0])
        for i in range(m):
            for j in range(n):
                c=sum(b[ii][jj]&1 for ii in range(max(0,i-1),min(i+2,m)) for jj in range(max(0,j-1),min(j+2,n)))
                if c==3 or c-b[i][j]==3: b[i][j]|=2
        for i in range(m):
            for j in range(n):
                b[i][j]>>=1