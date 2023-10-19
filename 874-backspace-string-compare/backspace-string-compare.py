class Solution:
    def backspaceCompare(self,s,t):
        n,m,s1,s2,s,t=len(s),len(t),[],[],list(s),list(t)
        for i in range(n):
            a=s.pop(0)
            if a!="#": s1.append(a)
            elif s1: s1.pop()
        for i in range(m):
            b=t.pop(0)
            if b!="#": s2.append(b)
            elif s2: s2.pop()
        return s1==s2