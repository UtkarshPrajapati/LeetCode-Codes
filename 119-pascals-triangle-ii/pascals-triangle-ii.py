class Solution:
    def getRow(self,n):
        dp={0:[1],1:[1,1]}
        for i in range(2,n+1):
            dp[i]=[1]+list(map(lambda x,y: x+y,dp[i-1][:-1],dp[i-1][1:]))+[1]
        return dp[n]