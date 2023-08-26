class Solution:
    def getSum(self,a,b):
        x,y=abs(a),abs(b)
        if x<y: a,b=b,a;x,y=y,x  
        if a*b>=0:
            while y: x,y=x^y,(x&y)<<1
        else:
            while y: x,y=x^y,(~x&y)<<1
        return x*(1 if a>0 else -1)