class Solution:
    def countAndSay(self,n):
        if n==1: return "1"
        if n==2: return "11"
        s=self.countAndSay(n-1)
        last,c,res=s[0],1,""
        for i in range(1,len(s)):
            if last==s[i]: c+=1
            else: res+=str(c)+last;last,c=s[i],1
        return res+str(c)+last