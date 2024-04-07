class Solution:
    def checkValidString(self,s):
        l=r=0
        for c in s:
            l+=1 if c=='(' else -1
            r+=1 if c!=')' else -1
            if r<0: break
            l=max(l,0)
        return l==0