class Solution:
    def searchMatrix(self,mat,t):
        l,r,rn=0,len(mat[0])-1,0
        while l<=r and 0<=rn<len(mat):
            if mat[rn][l]<=t<=mat[rn][r]:
                m=(l+r)//2
                if mat[rn][m]==t: return True
                elif mat[rn][m]>t: r=m-1
                else: l=m+1
            else: rn+=1
        return False