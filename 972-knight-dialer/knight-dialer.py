class Solution:
    def knightDialer(self,n):
        d,dp=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[4,2]],[1]*10
        for _ in range(n-1):
            dp=[(sum(dp[j] for j in d[i])%1000000007) for i in range(10)]
        return sum(dp)%1000000007