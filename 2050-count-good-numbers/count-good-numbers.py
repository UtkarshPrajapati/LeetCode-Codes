class Solution:
    def countGoodNumbers(self,n):
        m,t=1000000007,n//2
        return (pow(5,t+1,m)*pow(4,t,m))%m if n&1 else (pow(5,t,m)*pow(4,t,m))%m