class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        ma1,mi1=max(nums),min(nums)
        nums.remove(ma1)
        nums.remove(mi1)
        return (ma1*max(nums))-(mi1*min(nums))