class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid);n=len(grid[0])
        t=0
        for i in range(m):
            j=0
            while j<n and grid[i][j]>=0: j+=1
            t+=(n-j)
        return t