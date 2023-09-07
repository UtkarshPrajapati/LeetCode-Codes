class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums);l,r=0,n-1
        s,e=-1,-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target: l=m+1
            elif nums[m]>target: r=m-1
            else:
                s=e=m
                while s>0 and nums[s-1]==target: s-=1
                while e<n-1 and nums[e+1]==target: e+=1
                break
        return [s,e]