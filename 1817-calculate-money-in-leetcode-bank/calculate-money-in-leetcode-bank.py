class Solution:
    def totalMoney(self,n):
        s,a,b=0,n//7,n%7
        s+=7*(4*a+a*(a-1)//2)
        s+=(a+1)*b+(b-1)*b//2
        return s