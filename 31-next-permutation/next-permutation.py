class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        if n==1: return nums
        dec=False
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]: dec=True;break
        if not dec: nums[:]=nums[::-1];return nums
        n1=nums[i+1:]
        k=n-i-2-min(j for j in range(n-i-1) if n1[::-1][j]>nums[i])
        nums[i],nums[k+i+1]=nums[k+i+1],nums[i]
        nums[:]=nums[:i+1]+nums[i+1:][::-1]
        return nums