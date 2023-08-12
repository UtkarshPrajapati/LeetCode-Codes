class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1 if g[0][0]==0 else 0
        for i in range(m):
            for j in range(n):
                if g[i][j]==1: dp[i][j]=0
                else:
                    if j>0: dp[i][j]+=dp[i][j-1]
                    if i>0: dp[i][j]+=dp[i-1][j]
        return dp[m-1][n-1]