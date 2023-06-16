class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums)<=2: return 1
            l,r=[v for v in nums if v<nums[0]],[v for v in nums if v>nums[0]]
            return comb(len(l)+len(r),len(r))*f(l)*f(r)
        return (f(nums)-1)%(1000000007)