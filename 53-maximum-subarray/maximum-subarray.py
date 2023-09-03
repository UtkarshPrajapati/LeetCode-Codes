class Solution:
    def maxSubArray(self,nums):
        s,ms=0,float('-inf')
        for i in nums:
            s+=i
            ms=max(s,ms)
            if s<0: s=0
        return ms