class Solution:
    def minOperations(self, s: str) -> int:
        a=f=0
        for c in s:
            if int(c)!=f: a+=1
            f=not f
        return min(a,len(s)-a)