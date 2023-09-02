class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp=[0]+[len(s)+1]*len(s)
        d=set(dictionary)
        for i in range(1,len(s)+1):
            dp[i]=dp[i-1]+1
            for l in range(1, i + 1): 
                if s[i-l:i] in d:
                    dp[i] = min(dp[i], dp[i-l])           
        return dp[-1]