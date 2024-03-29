class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums);dp=[[0]*n]*n 
        for i in range(n-1,-1,-1): 
            for j in range(i,n): 
                if i==j:  dp[i][j]=nums[i] 
                else: dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])    
        return dp[0][n-1]>=0 