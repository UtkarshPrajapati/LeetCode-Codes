class Solution:
    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        mod,dp,index=1000000007,[1]*len(arr), {x: i for i, x in enumerate(arr)}
        for x,i in index.items():
            for j in range(i):
                if x%arr[j]==0:
                    q=x//arr[j] 
                    if q in index: dp[i]=(dp[i]%mod+(dp[j]*dp[index[q]])%mod)%mod
        return sum(dp)%mod