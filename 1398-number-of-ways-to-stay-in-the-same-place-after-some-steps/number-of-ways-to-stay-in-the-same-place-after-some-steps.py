class Solution:
    def numWays(self,steps,arrLen):
        maxPos=min(arrLen,steps//2+1)
        @cache
        def dfs(pos,s):
            if pos==0 and s==0: return 1
            if pos<0 or pos==maxPos or s<0: return 0
            return dfs(pos+1,s-1)+dfs(pos-1,s-1)+dfs(pos,s-1)
        return dfs(0,steps)%1000000007