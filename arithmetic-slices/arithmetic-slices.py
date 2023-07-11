class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums);c=0;dp=0
        for i in range(2,n):
            x,y,z=nums[i],nums[i-1],nums[i-2]
            dp=(dp+1)*(x+z==2*y);c+=dp
        return c