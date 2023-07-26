class Solution:
    def minSpeedOnTime(self, d, t):
        if (n:=len(d))>=t+1: return -1
        i,j=1,max(max(d),ceil(d[n-1]/(t-n+1)))
        while i<j:
            m=(i+j)//2
            if sum(ceil(d/m) for d in d[:n-1])+d[n-1]/m<=t: j=m
            else: i=m+1
        return j