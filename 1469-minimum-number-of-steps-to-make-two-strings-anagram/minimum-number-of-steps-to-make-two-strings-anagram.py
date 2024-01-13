class Solution:
    def minSteps(self,s,t):
        c1,c2,ans=Counter(s),Counter(t),0
        for ch in c1:
            if ch in c2:
                if c1[ch]>c2[ch]: ans+=c1[ch]-c2[ch]
            else: ans+=c1[ch]
        return ans