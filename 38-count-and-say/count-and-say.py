class Solution:
    def countAndSay(self,n):
        if n==1: return "1"
        s=self.countAndSay(n-1)
        res,c="",1
        for i in range(1,len(s)):
            if s[i-1]==s[i]: c+=1
            else: res+=str(c)+s[i-1];c=1
        return res+str(c)+s[-1]