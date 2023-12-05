class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ch=co=0
        while ch<len(g) and co<len(s):
            if s[co]>=g[ch]: ch+=1
            co+=1
        return ch