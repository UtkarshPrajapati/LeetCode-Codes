class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [j for i in range(0,len(nums),2) for j in [nums[i+1]]*nums[i]]