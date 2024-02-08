class Solution:
    def numSquares(self,n):
        sqr = int(n**0.5)
        if sqr*sqr==n or any((n-i*i)**0.5%1==0 for i in range(1,sqr+1)): return 1 if sqr*sqr==n else 2
        while n%4==0: n//=4
        return 4 if n%8==7 else 3