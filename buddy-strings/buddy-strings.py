class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        if s==goal: return len(set(s))<len(s)
        d=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                d.append(i)
                if len(d)>2: return False
        return len(d)==2 and s[d[0]]==goal[d[1]] and s[d[1]]==goal[d[0]]
