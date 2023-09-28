class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a,i=[],0
        while i<len(nums):
            if nums[i]%2==0: a.append(nums.pop(i))
            else: i+=1
        return a+nums