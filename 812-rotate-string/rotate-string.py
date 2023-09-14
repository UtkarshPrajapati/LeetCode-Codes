class Solution:
    def rotateString(self,s,goal):
        n,m=len(s),len(goal)
        if n>m: return False
        s*=2
        for i in range(2*n-m):
            if s[i:i+m]==goal: return True
        return False