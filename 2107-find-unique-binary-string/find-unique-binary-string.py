class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums=set(nums)
        n=len(nums)
        for i in range(2**n):
            a=bin(i)[2:].zfill(n)
            if a not in nums: return a