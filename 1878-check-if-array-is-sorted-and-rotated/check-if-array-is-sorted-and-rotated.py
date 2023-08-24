class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                k=i+1
                break
        na=nums[k:]+nums[:k]
        for i in range(len(na)-1):
            if na[i+1]<na[i]: return False
        return True