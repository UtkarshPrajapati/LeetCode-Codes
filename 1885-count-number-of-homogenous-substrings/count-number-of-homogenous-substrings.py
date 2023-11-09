class Solution:
    def countHomogenous(self, s: str) -> int:
        ans,a=0,1
        for i in range(1,len(s)):
            if s[i]==s[i-1]: a+=1
            else: ans+=a*(a+1)//2;a=1
        return (ans+a*(a+1)//2)%1000000007