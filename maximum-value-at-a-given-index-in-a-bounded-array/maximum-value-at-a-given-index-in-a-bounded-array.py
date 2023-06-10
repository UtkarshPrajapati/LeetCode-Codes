class Solution:
    def maxValue(self, n, index, maxSum):
        def check(a):
            lo,ro=max(a-index,0),max(a-((n-1)-index),0)
            return (a+lo)*(a-lo+1)//2+(a+ro)*(a-ro+1)//2-a
        maxSum-=n
        l,r=0,maxSum
        while l<r:
            mid=(l+r+1)//2
            l,r=(mid,r) if check(mid)<=maxSum else (l,mid-1)
        return l+1