class Solution:
    def maxDepth(self, s: str) -> int:
        c,m=0,0
        for i in s:
            if i=='(': c+=1;m=max(m,c)
            elif i==')': c-=1
        return m