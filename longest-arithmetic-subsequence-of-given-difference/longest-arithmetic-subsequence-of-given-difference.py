class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        dp={}
        for i in arr: dp[i]=dp.get(i-d,0)+1
        return max(dp.values())