class Solution:
    def gameOfLife(self,b):
        m,n=len(b),len(b[0])
        for i in range(m):
            for j in range(n):
                s=sum(b[x][y]&1 for x in range(max(0,i-1),min(i+2,m)) for y in range(max(0,j-1),min(j+2,n)))
                if b[i][j]==1 and (s==3 or s==4): b[i][j]|=2
                if b[i][j]==0 and s==3: b[i][j]|=2
        for i in range(m):
            for j in range(n):
                b[i][j]>>=1