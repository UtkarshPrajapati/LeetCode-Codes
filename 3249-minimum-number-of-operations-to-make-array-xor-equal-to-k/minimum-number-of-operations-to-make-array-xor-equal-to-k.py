class Solution:
    def minOperations(self,nums,k):
        fx=reduce(xor,nums)
        m=len(bin(k if k>fx else fx))-2
        return sum(i!=j for i,j in zip(bin(fx)[2:].zfill(m),bin(k)[2:].zfill(m)))