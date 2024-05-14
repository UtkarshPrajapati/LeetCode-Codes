class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n,vis,dirs=len(grid),len(grid[0]),set(),[(1,0),(-1,0),(0,1),(0,-1)]
        def f(i,j,vis):
            return grid[i][j]+max([f(i+di,j+dj,vis|{(i,j)}) for di,dj in dirs if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]!=0 and (i+di,j+dj) not in vis],default=0)
        return max([f(i,j,vis) for i in range(m) for j in range(n) if grid[i][j]!=0],default=0)