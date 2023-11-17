class Solution:
    def minPairSum(self,nums):
        nums.sort()
        return max(nums[i]+nums[-(i+1)] for i in range(len(nums)//2))