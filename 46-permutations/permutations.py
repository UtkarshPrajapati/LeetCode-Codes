class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [p[:i] + [nums[0]] + p[i:] for p in self.permute(nums[1:]) for i in range(len(nums))] or [[]]
