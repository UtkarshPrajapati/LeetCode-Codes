class Solution:
    def minSteps(self,s,t):
        c,ans=[0]*26,0
        for cs in s:
            c[ord(cs)-97]+=1
        for ct in t:
            c[ord(ct)-97]-=1
        for cnt in c:
            if cnt>0: ans+=cnt
        return ans