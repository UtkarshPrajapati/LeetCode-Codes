class Solution:
    def shipWithinDays(self,w,d):
        def f(maxw):
            c,nd=0,1
            for i in w:
                c+=i
                if c>maxw: c=i;nd+=1
            return nd<=d
        l,r=max(w),sum(w)
        while l<r:
            m=(l+r)//2
            if f(m): r=m
            else: l=m+1
        return l