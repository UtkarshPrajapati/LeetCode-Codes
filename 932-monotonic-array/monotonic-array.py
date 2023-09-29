class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3: return True
        def mi(nums):
            f=True
            for i in range(n-1): 
                if nums[i]>nums[i+1]: f=False
            return f
        def md(nums):
            f=True
            for i in range(n-1): 
                if nums[i]<nums[i+1]: f=False
            return f
        return mi(nums) or md(nums)