class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0": return 0
        n=len(s);dp=[1,1]+[0]*(n-1)             
        for i in range(2,n+1):
            if 1<=int(s[i-1])<=9: dp[i]+=dp[i-1]
            if 10<=int(s[i-2]+s[i-1])<=26: dp[i]+=dp[i-2] 
        return dp[-1]