class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=set(nums)
        for i in a:
            if nums.count(i)%2==1: return False
        return True