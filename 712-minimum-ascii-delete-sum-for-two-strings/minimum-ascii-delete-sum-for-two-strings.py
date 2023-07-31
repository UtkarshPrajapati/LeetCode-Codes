class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp={}
        def f(i,j):
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)]=0 if i<0 and j<0 else ord(s2[j])+f(i,j-1) if i<0 else ord(s1[i])+f(i-1,j) if j<0 else f(i-1,j-1) if s1[i]==s2[j] else min(ord(s1[i])+f(i-1,j),ord(s2[j])+f(i,j-1))
            return dp[(i,j)]
        return f(len(s1)-1,len(s2)-1)