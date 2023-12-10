class Solution:
    def transpose(self,matrix):
        m,n=len(matrix),len(matrix[0])
        mat=[[None]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                mat[i][j]=matrix[j][i]
        return mat