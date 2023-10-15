class Solution:
    def numWays(self,steps,arrLen):
        @cache
        def dfs(cur,s):
            if not cur and not s: return 1
            if cur<0 or cur==arrLen or s<0: return 0
            return dfs(cur+1,s-1)+dfs(cur-1,s-1)+dfs(cur,s-1)
        return dfs(0,steps)%1000000007