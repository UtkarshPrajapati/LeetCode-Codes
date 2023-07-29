class Solution:
    def soupServings(self, n: int) -> float:
        if n>4450: return 1
        d,n={},(n+24)//25
        return (f:=lambda i,j: d[(i,j)] if (i,j) in d else 0.5 if i<=0 and j<=0 else 1 if i<=0 else 0 if j<=0 else d.setdefault((i,j),sum(f(i+k-4,j-k) for k in range(4))/4))(n,n)