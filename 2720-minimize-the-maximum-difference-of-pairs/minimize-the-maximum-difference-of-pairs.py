class Solution:
    def minimizeMax(self,nums,p):
        nums.sort()
        l,r=0,nums[-1]-nums[0]
        while l<r:
            m,c,i=(l+r)//2,0,0
            while i<len(nums)-1 and c<p:
                c,i=(c+1,i+2) if nums[i+1]-nums[i]<=m else (c,i+1)
            l,r=(l,m) if c>=p else (m+1,r)
        return l