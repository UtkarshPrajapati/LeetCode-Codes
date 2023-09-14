class Solution:
    def splitArray(self,nums,k):
        def f(i):
            cursum,subar=0,0
            for n in nums:
                cursum+=n
                if cursum>i: subar+=1;cursum=n
            return subar+1<=k
        l,r,ans=max(nums),sum(nums),float("inf")
        while l<=r:
            mid=(l+r)//2
            if f(mid): ans=mid;r=mid-1
            else: l=mid+1
        return ans