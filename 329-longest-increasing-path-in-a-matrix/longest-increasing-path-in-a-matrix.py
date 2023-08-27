class Solution:
    def longestIncreasingPath(self,mat):
        m,n=len(mat),len(mat[0])
        dp=[[0]*n for _ in range(m)]
        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n: return 0
            if dp[i][j]: return dp[i][j]
            c=mat[i][j]
            cnt=1
            if j-1>=0 and c<mat[i][j-1]: cnt=max(cnt,f(i,j-1)+1)
            if j+1<n and c<mat[i][j+1]: cnt=max(cnt,f(i,j+1)+1)
            if i-1>=0 and c<mat[i-1][j]: cnt=max(cnt,f(i-1,j)+1)
            if i+1<m and c<mat[i+1][j]: cnt=max(cnt,f(i+1,j)+1)
            dp[i][j]=cnt
            return cnt
        return max(f(i,j) for i in range(m) for j in range(n))