class Solution:
    def minDays(self,b,m,k):
        n=len(b)
        if m*k>n: return -1
        def f(day):
            c,nb=0,0
            for i in b:
                c=0 if i>day else c+1
                if c==k: nb,c=nb+1,0
            return nb>=m
        l,r=min(b),max(b)
        while l<=r:
            mid=(l+r)//2
            if f(mid): r=mid-1
            else: l=mid+1
        return l