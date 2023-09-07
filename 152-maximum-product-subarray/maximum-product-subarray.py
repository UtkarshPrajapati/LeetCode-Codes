class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma, mi, res = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            temp_ma=ma
            ma=max(i,ma*i,mi*i)
            mi=min(i,temp_ma*i,mi*i)
            res=max(res, ma)
        return res