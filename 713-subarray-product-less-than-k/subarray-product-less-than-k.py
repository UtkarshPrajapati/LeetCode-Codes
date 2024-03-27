class Solution:
    def numSubarrayProductLessThanK(self,nums,k):
        if k<=1: return 0
        l,r,p,ans=0,0,1,0
        n=len(nums)
        while r<n:
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            ans+=r-l+1
            r+=1
        return ans