class Solution:
    def countOrders(self,n):
        c=1
        for i in range(2,n+1):
            c*=(2*i-1)*i
        return c%1000000007