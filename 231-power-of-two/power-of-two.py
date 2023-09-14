class Solution:
    def isPowerOfTwo(self,n):
        if not n or n&(n-1): return False
        return True
        