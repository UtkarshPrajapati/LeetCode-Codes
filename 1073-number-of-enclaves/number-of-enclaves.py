class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n,v=len(grid),len(grid[0]),set()
        q=deque((i,j) for i in range(m) for j in range(n) if grid[i][j]==1 and (i in [0,m-1] or j in [0, n-1]))
        while q:
            x,y=q.popleft()
            if (x,y) in v: continue
            v.add((x,y))
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1: q.append((nx,ny))
        for x,y in v:
            grid[x][y]=0
        return sum(sum(row) for row in grid)