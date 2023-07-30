class Solution:
    def strangePrinter(self, s: str) -> int:
        s="".join(k for k,_ in groupby(s))
        @cache
        def f(i,j):
            if i==j: return 0
            t=1+f(i+1,j)
            if (l:=[f(i,m)+f(m+1,j) for m in range(i+1,j) if s[i]==s[m]]): t=min(t,min(l))
            return t
        return f(0,len(s))