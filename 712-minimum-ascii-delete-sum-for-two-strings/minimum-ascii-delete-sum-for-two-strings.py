class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp=[0]*len(s2)
        for c1 in s1:
            prev=0
            for i,c2 in enumerate(s2):
                last,dp[i]=dp[i],prev+ord(c1) if c1==c2 else max(dp[i],prev)
                prev=max(prev,last)
        return sum(map(ord,f'{s1}{s2}'))-2*max(dp)