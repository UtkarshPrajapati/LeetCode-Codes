class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i])-sum(nums[i+1:])) for i in range(len(nums))]