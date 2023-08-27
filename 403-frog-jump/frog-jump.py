class Solution:
    def canCross(self,stones):
        n=len(stones)
        dp=[[False]*(n+1) for _ in range(n)]
        dp[0][0]=True
        s=set(stones)
        si={stone:i for i,stone in enumerate(stones)}
        for i in range(n-1):
            for j in range(n+1):
                if dp[i][j]:
                    for k in [j-1,j,j+1]:
                        if stones[i]+k in s: dp[si[stones[i]+k]][k]=True
        return any(dp[n-1])