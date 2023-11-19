class Solution:
    def reductionOperations(self,nums):
        nums.sort(reverse=True)
        return sum(i for i in range(1,len(nums)) if nums[i]!=nums[i-1])