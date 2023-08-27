class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        s=self.countAndSay(n-1)
        last=s[0]
        c=1
        res=""
        for i in range(1,len(s)):
            if last==s[i]: c+=1
            else:
                res+=str(c)+str(last)
                last=s[i]
                c=1
        res+=str(c)+str(last)
        return res