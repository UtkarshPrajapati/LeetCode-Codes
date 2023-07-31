class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1,n2,dp=len(s1),len(s2),{}
        def f(i,j):
            if (i,j) in dp: return dp[(i,j)]
            if i<0 and j<0: return 0
            if i<0: dp[(i,j)] = ord(s2[j])+f(i,j-1)
            elif j<0: dp[(i,j)] = ord(s1[i])+f(i-1,j)
            else: dp[(i,j)] = f(i-1,j-1) if s1[i]==s2[j] else min(ord(s1[i])+f(i-1,j),ord(s2[j])+f(i,j-1))
            return dp[(i,j)]
        return f(n1-1,n2-1)