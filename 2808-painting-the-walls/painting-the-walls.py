class Solution:
    def paintWalls(self, cost, time):
        n=len(cost);dp=[0]+[sum(cost)]*n
        for i,c in enumerate(cost):
            for t in range(n,0,-1):
                dp[t]=min(dp[t],dp[max(t-time[i]-1,0)]+c)
        return dp[-1]