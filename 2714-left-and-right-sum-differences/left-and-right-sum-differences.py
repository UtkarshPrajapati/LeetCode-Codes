class Solution:
    def leftRightDifference(self, nums):
        ls,rs,r=0,sum(nums),[]
        for i in nums:
            rs-=i
            r+=[abs(ls-rs)]
            ls+=i
        return r