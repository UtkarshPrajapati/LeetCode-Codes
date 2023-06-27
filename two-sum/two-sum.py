class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        d={}
        for i,n in enumerate(nums):
            m=t-n
            if m in d: return [d[m], i]
            d[n]=i