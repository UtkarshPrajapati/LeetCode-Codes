class Solution:
    def findErrorNums(self, nums):
        s=sum(set(nums))
        n=len(nums)
        return [sum(nums)-s,n*(n+1)//2-s]