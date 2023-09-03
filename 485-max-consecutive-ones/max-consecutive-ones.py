class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,j=[0]*len(nums),0
        for i in nums:
            if i==1: c[j]+=1
            else: j+=1
        return max(c)