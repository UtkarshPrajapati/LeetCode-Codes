class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s=sum(rods);dp=[0]+[-1]*s
        for rod in rods:
            dp_copy = dp[:]
            for i in range(s - rod + 1):
                if dp_copy[i] < 0: continue
                dp[i + rod] = max(dp[i + rod], dp_copy[i])
                dp[abs(i - rod)] = max(dp[abs(i - rod)], dp_copy[i] + min(i, rod))
        return dp[0]