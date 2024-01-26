class Solution:
    def findPaths(self,m,n,N,x,y):
        dp=[[0]*n for _ in range(m)]
        dp[x][y]=1
        c=0
        for moves in range(1,N+1):
            temp=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for _ in range(sum([i==m-1,j==n-1,i==0,j==0])): c=(c+dp[i][j])%1000000007
                    temp[i][j]=((dp[i-1][j] if i>0 else 0)+(dp[i+1][j] if i<m-1 else 0)+(dp[i][j-1] if j>0 else 0)+(dp[i][j+1] if j<n-1 else 0))%1000000007
            dp=temp
        return c