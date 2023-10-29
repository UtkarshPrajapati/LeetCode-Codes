class Solution:
    def findKthBit(self,n,k):
        if n==k==1: return "0"
        if k==2**(n-1): return "1"
        s="0"
        for _ in range(ceil(log2(k+1))):
            s+="1"+''.join('0' if bit=='1' else '1' for bit in s)[::-1]
        return s[k-1]