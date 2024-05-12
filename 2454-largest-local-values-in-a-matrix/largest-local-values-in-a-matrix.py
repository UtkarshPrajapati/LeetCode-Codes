class Solution:
    def largestLocal(self,grid):
        n=len(grid)
        return [[max(grid[i+x][j+y] for x in [-1,0,1] for y in [-1,0,1]) for j in range(1,n-1)] for i in range(1,n-1)]