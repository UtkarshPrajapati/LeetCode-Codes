class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ind,num in enumerate(nums):
            idx=abs(num)
            if nums[idx]<0: return idx
            nums[idx]=-nums[idx]
        return ind