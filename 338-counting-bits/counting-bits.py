class Solution:
    def countBits(self,n):
        return [i.bit_count() for i in range(n+1)]