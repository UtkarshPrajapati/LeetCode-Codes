class Solution:
    def isPowerOfFour(self,n):
        if n<1: return False
        a=log(n,4)
        return True if a==int(a) else False