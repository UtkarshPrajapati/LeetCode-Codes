class Solution:
    def canJump(self,nums):
        l=len(nums)-1
        for i in range(l-1,-1,-1):
            if nums[i]>=l-i: l=i
        return l==0