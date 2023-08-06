class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp=[[0 for _ in range(n+1)] for _ in range(2)];dp[0][0]=1
        for i in range(1,goal+1):
            dp[i&1][0]=0
            for j in range(1,min(i,n)+1):
                dp[i&1][j]=dp[(i-1)&1][j-1]*(n-(j-1))%1000000007
                if j>k: dp[i&1][j]=(dp[i&1][j]+dp[(i-1)&1][j]*(j-k))%1000000007
        return dp[goal&1][n]