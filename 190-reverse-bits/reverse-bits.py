class Solution:
    def reverseBits(self, n: int) -> int:
        i,c=31,0
        while n:
            c+=(n&1)<<i
            i-=1
            n>>=1
        return c