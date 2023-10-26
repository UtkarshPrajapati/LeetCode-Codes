class Solution:
    def numFactoredBinaryTrees(self,arr):
        MOD=1000000007
        arr.sort()
        dp=[1]*len(arr)
        index={x:i for i,x in enumerate(arr)}
        for i,x in enumerate(arr):
            for j in range(i):
                if x%arr[j]==0 and x/arr[j] in index: dp[i]=(dp[i]+dp[j]*dp[index[x/arr[j]]])%MOD
        return sum(dp)%MOD