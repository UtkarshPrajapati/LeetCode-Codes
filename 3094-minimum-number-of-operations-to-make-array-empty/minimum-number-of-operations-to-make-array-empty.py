class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m=0
        c=Counter(nums)
        it=c.items()
        for n,cnt in it:
            dp=[float('inf')]*(cnt+1)
            dp[0]=0
            for i in range(cnt+1):
                if i>=2: dp[i]=min(dp[i],dp[i-2]+1)
                if i>=3: dp[i]=min(dp[i],dp[i-3]+1)
            if dp[cnt]==float('inf'): return -1
            m+=dp[cnt]
        return m