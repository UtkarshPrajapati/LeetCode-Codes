class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1,n2=len(s1),len(s2)
        dp={}
        def f(i,j):
            if (i,j) in dp: return dp[(i,j)]
            if i<0: dp[(i,j)] = sum(ord(ch) for ch in s2[:j+1])
            elif j<0: dp[(i,j)] = sum(ord(ch) for ch in s1[:i+1])
            elif s1[i]==s2[j]: dp[(i,j)] = f(i-1,j-1)
            else: dp[(i,j)] = min(ord(s1[i])+f(i-1,j),ord(s2[j])+f(i,j-1))
            return dp[(i,j)]
        return f(n1-1,n2-1)
