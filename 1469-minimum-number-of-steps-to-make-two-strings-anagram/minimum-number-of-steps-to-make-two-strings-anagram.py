class Solution:
    def minSteps(self,s,t):
        c,ans=[0]*26,0
        for cs,ct in zip(s,t):
            c[ord(cs)-97]+=1
            c[ord(ct)-97]-=1
        for count in c:
            if count>0: ans+=count
        return ans