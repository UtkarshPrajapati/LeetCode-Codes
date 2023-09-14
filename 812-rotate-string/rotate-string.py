class Solution:
    def rotateString(self,s,goal):
        n,m=len(s),len(goal)
        if n!=m: return False
        for i in range(n):
            if s[i:]+s[:i]==goal: return True
        return False