class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mc,c=0,0
        for i in nums:
            if i==1: c+=1
            else: mc=max(c,mc);c=0
        return max(c,mc)