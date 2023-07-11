class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp=0
        return sum(dp:=(dp+1)*(nums[i]+nums[i-2]==2*nums[i-1]) for i in range(2,len(nums)))