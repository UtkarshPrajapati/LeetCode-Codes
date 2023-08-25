class Solution:
    def uniquePaths(self,m,n):
        a=[1]*n
        for i in range(m-1):
            b=[1]*n
            for j in range(n-2,-1,-1): b[j]=b[j+1]+a[j]
            a=b 
        return a[0]