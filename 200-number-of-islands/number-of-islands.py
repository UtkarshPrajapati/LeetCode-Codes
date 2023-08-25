class Solution:
    def numIslands(self,grid):
        if not grid:return 0
        m,n,c=len(grid),len(grid[0]),0
        def f(grid,i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0': return
            grid[i][j]='0'
            f(grid,i+1,j)
            f(grid,i-1,j)
            f(grid,i,j+1)
            f(grid,i,j-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    f(grid,i,j)
                    c+=1
        return c