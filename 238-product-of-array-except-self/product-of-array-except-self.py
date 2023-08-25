class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums);res=[1]*n
        l=r=1
        for i in range(n):
            res[i]*=l
            res[n-i-1]*=r
            l*=nums[i]
            r*=nums[n-i-1]
        return res