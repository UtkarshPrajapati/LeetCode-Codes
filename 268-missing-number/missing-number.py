class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=list(range(0,len(nums)+1))
        for i in x:
            if i not in nums: return i