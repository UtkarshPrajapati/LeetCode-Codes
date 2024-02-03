class Solution:
    def maxSumAfterPartitioning(self,arr,k):
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=max(dp[i-j]+max(arr[i-j:i])*j for j in range(1,min(k,i)+1))
        return dp[n]