class Solution:
    def change(self,amt,coins):
        dp=[1]+[0]*amt
        for i in coins:
            for j in range(i,amt+1): dp[j]+=dp[j-i]
        return dp[amt]