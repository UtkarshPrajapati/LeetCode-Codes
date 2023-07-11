class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n,c,dp=len(nums),0,0
        for i in range(2,n):
            c+=(dp:=dp+1 if nums[i]+nums[i-2]==2*nums[i-1] else 0)
        return c