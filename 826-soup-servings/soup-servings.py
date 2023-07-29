class Solution:
    def soupServings(self, n: int) -> float:
        if n>4450: return 1
        d,n={},(n+24)//25
        def dp(i,j):
            if (i,j) in d: return d[(i,j)]
            if i<=0 and j<=0: return 0.5
            if i<=0: return 1
            if j<=0: return 0
            return d.setdefault((i,j),sum(dp(i+k-4,j-k) for k in range(4))/4)
        return dp(n,n)