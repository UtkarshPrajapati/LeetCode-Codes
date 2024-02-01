class Solution:
    def divideArray(self, nums, k):
        size=len(nums)
        nums.sort()
        result,gi=[],0
        for i in range(0,size,3):
            if i+2<size and nums[i+2]-nums[i]<=k:
                result.append([nums[i],nums[i+1],nums[i+2]])
                gi+=1
            else: return []
        return result