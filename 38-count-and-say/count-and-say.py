class Solution:
    def countAndSay(self, n):
        if n==1: return "1"
        s=self.countAndSay(n-1)
        res,i="",0
        while i<len(s):
            count=1
            while i+1<len(s) and s[i]==s[i+1]:
                i+=1;count+=1
            res+=str(count)+s[i];i+=1
        return res