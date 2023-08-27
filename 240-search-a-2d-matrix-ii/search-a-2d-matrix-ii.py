class Solution:
    def searchMatrix(self,mat,t):
        m,n=len(mat),len(mat[0])
        r,c=0,n-1
        while r<m and c>=0:
            if mat[r][c]==t: return True
            elif mat[r][c]>t: c-=1
            else: r+=1
        return False