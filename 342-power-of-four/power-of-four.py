class Solution:
    def isPowerOfFour(self,n):
        return n>0 and n&0xAAAAAAAA==0 and n&(n-1)==0