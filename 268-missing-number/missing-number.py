class Solution:
    def missingNumber(self,nums):
        for i in list(range(0,len(nums)+1)):
            if i not in nums: return i