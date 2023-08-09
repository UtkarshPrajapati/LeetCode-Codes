class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l,r=0,nums[-1]-nums[0]
        while l<r:
            mid,cnt,i=(l+r)//2,0,0
            while i<len(nums)-1 and cnt<p:
                cnt,i=(cnt+1,i+2) if nums[i+1]-nums[i]<=mid else (cnt,i+1)
            l,r=(l,mid) if cnt>=p else (mid+1,r)
        return l