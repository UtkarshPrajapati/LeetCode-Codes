class Solution:
    def canCross(self,stones):
        n=len(stones)
        dp={stone:set() for stone in stones}
        dp[0].add(0)
        for i in range(n):
            for k in dp[stones[i]]:
                for step in [k-1,k,k+1]:
                    if step and stones[i]+step in dp:
                        dp[stones[i]+step].add(step)
                        if stones[i]+step==stones[-1]: return True
        return False