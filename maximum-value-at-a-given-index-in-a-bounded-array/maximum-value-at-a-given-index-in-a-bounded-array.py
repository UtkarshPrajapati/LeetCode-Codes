class Solution:
    def check(self, a):
        lo,ro=max(a-self.index,0),max(a-((self.n-1)-self.index),0)
        return (a+lo)*(a-lo+1)//2+(a+ro)*(a-ro+1)//2-a
    def maxValue(self, n, index, maxSum):
        self.n,self.index=n,index
        maxSum-=n
        l,r=0,maxSum
        while l<r:
            mid=(l+r+1)//2
            l,r=(mid,r) if self.check(mid)<=maxSum else (l,mid-1)
        return l+1