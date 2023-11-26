class Solution:
    def largestSubmatrix(self,matrix):
        m,n,res=len(matrix),len(matrix[0]),0
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]==1: matrix[i][j]+=matrix[i-1][j]
        for i in range(m):
            row=sorted(matrix[i],reverse=True)
            a=[row[j]*(j+1) for j in range(n)]
            res=max(res,max(a) if a else 0)
        return res