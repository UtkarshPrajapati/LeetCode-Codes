class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        grid=[[1-val for val in row] if row[0]==0 else row for row in grid]
        for j in range(1,n):
            if sum(grid[i][j] for i in range(m))<m/2:
                for i in range(m):
                    grid[i][j]=1-grid[i][j]
        return sum(int(''.join(map(str,row)),2) for row in grid)