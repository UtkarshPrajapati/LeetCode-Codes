class Solution:
    def isPowerOfFour(self,n):
        if n<1: return False
        while n!=1:
            n,r=divmod(n,4)
            if r!=0: return False
        return True