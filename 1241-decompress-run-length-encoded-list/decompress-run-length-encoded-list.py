class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums),2):
            l+=[nums[i+1]]*nums[i]
        return l