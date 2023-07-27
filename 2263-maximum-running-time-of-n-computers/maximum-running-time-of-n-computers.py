class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        s=sum(bat);i,j=1,s//n;l=len(bat)
        if l<n: return 0
        if l==n: return min(bat)
        if n==1: return s
        if j>=max(bat): return j
        while i<j: 
            t=j-(j-i)//2 
            if sum(min(b,t) for b in bat)<t*n: j=t-1 
            else: i=t
        return i