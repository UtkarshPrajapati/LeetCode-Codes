class Solution:
    def check(self, a):
        lo=max(a-self.index,0)
        res=(a+lo)*(a-lo+1)//2
        ro=max(a-((self.n-1)-self.index),0)
        res+=(a+ro)*(a-ro+1)//2
        return res-a
    def maxValue(self, n, index, maxSum):
        self.n,self.index=n,index
        maxSum-=n
        left,right=0,maxSum
        while left<right:
            mid=(left+right+1)//2
            if self.check(mid)<=maxSum: left=mid
            else: right=mid-1
        return left+1