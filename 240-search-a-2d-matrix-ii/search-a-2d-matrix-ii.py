class Solution:
    def searchMatrix(self,mat,t):
        m,n=len(mat),len(mat[0])
        r,c=[],[]
        for i in range(m):
            if mat[i][0]<=t<=mat[i][n-1]: r.append(i)
        for j in range(n):
            if mat[0][j]<=t<=mat[m-1][j]: c.append(j)
        print(r,c)
        for i in r:
            for j in c:
                if mat[i][j]==t: return True
        return False