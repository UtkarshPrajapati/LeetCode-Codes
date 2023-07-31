class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1,n2=len(s1),len(s2);i,j=n1,n2
        @cache
        def f(i,j):
            if i<0: return sum(ord(ch) for ch in s2[:j+1])
            if j<0: return sum(ord(ch) for ch in s1[:i+1])
            if s1[i]==s2[j]: return f(i-1,j-1)
            else: return min(ord(s1[i])+f(i-1,j),ord(s2[j])+f(i,j-1),ord(s1[i])+ord(s2[j])+f(i-1,j-1))
        return f(n1-1,n2-1)