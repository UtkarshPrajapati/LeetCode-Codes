class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        fx=0
        for i in nums:
            fx^=i
        xb=bin(fx)[2:].zfill(len(bin(k))-2)
        kb=bin(k)[2:].zfill(len(bin(fx))-2)
        c=0
        for i,j in zip(xb,kb):
            if i!=j: c+=1
        return c