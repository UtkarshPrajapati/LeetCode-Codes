class Solution:
    def soupServings(self, n: int) -> float:
        if n>4450: return 1
        d,n={},(n+24)//25
        def dp(i,j):
            if (i,j) in d: return d[(i,j)]
            if i<=0 and j<=0: return 0.5
            if i<=0: return 1
            if j<=0: return 0
            d[(i,j)]=0.25*(dp(i-4,j)+dp(i-3,j-1)+dp(i-2,j-2)+dp(i-1,j-3))
            return d[(i,j)]
        return dp(n,n)