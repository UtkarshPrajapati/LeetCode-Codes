class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l=r=k;ms=m=nums[k];n=len(nums)
        while l>0 or r<n-1:
            if l==0 or (r<n-1 and nums[r+1]>nums[l-1]): 
                r+=1
                m=min(m,nums[r])
            else: 
                l-=1
                m=min(m,nums[l])
            if m*(r-l+1)>ms: ms=m*(r-l+1)
        return ms