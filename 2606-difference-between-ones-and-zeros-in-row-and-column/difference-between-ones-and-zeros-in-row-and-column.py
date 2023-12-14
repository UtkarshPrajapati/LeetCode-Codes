class Solution:
    def onesMinusZeros(self,grid):
        m,n=len(grid),len(grid[0]);s=m+n
        r1,c1=[sum(i) for i in grid],[sum(j) for j in zip(*grid)]
        return [[2*(r1[i]+c1[j])-s for j in range(n)] for i in range(m)]