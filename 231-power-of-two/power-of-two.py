class Solution:
    def isPowerOfTwo(self,n):
        if n==0 or n&(n-1): return False
        return True