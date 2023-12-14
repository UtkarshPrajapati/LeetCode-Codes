class Solution:
    def minMoves(self, t: int, m: int) -> int:
        if m==0: return t-1
        c=0
        while t!=1:
                if t%2: t-=1
                else: t//=2;m-=1
                if m<1: return c+t
                c+=1
        return c