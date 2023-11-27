class Solution:
    def knightDialer(self,n):
        A,B,C,D=1,2,4,2
        if n==1: return A+B+C+D+1
        for i in range(n-1):
            A,B,C,D=B,2*A+C,(B+D)*2,C
        return (A+B+C+D)%1000000007