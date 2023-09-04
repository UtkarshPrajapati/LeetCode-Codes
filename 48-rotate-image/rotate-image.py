class Solution:
    def rotate(self,mat):
        n=len(mat[0])
        for j in range(n):
            for i in range(j+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for j in range(len(mat)):
            mat[j].reverse()