class Solution:
    def totalMoney(self,n):
        a,b=n//7,n%7
        return 7*(4*a+a*(a-1)//2)+(a+1)*b+(b-1)*b//2