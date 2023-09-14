class Solution:
    def searchMatrix(self,mat,t):
        mat=[j for i in mat for j in i]
        l,r=0,len(mat)-1
        while l<=r:
            if t==mat[(m:=(l+r)//2)]: return True
            l,r=(m+1,r) if t>mat[m] else (l,m-1)
        return False