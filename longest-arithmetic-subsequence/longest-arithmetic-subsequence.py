class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums);m=2
        if n<3: return n
        dp=[{} for _  in range(n)]
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                dp[i][d]=dp[j].get(d,1)+1
                m=max(m,dp[i][d])
        return m