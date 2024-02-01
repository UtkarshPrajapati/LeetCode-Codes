class Solution:
    def divideArray(self, nums, k):
        size,res=len(nums),[]
        nums.sort()
        for i in range(0,size,3):
            if i+2<size and nums[i+2]-nums[i]<=k: res.append([nums[i],nums[i+1],nums[i+2]])
            else: return []
        return res