class Solution:
    def findPeakGrid(self,mat):
        m,n=len(mat),len(mat[0])
        l,r=0,m-1
        while l<r:
            mid=(l+r)//2
            col=max(range(n),key=lambda j:mat[mid][j])
            if mat[mid][col]<mat[mid+1][col]: l=mid+1
            else: r=mid
        return [l,max(range(n),key=lambda j:mat[l][j])]