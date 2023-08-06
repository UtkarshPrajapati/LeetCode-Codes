class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1 or n>=len(s): return s
        res,i,step=['']*n,0,1
        for ch in s:
            res[i]+=ch
            i+=step
            if i in [0,n-1]: step=-step
        return ''.join(res)