class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);dp=[int(g[0][0]==0)]+[0]*(n-1)
        for i in range(m):
            for j in range(n):
                if g[i][j]==1: dp[j]=0
                else:
                    if j>0: dp[j]+=dp[j-1]
        return dp[n-1]