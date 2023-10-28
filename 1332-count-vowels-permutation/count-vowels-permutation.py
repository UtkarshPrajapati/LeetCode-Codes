class Solution:
    def countVowelPermutation(self,n):
        MOD = 10**9 + 7
        dp = [[1]*5 for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][1]+dp[i-1][2]+dp[i-1][4]
            dp[i][1]=dp[i-1][0]+dp[i-1][2]
            dp[i][2]=dp[i-1][1]+dp[i-1][3]
            dp[i][3]=dp[i-1][2]
            dp[i][4]=dp[i-1][2]+dp[i-1][3]
        # print(dp)
        return sum(dp[n-1])%MOD