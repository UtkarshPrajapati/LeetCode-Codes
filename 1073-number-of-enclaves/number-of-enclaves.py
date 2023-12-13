class Solution:
    def numEnclaves(self,grid):
        m,n,v,q,c=len(grid),len(grid[0]),set(),deque(),0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    c+=1
                    if i in [0,m-1] or j in [0, n-1]: q.append((i,j))
        while q:
            x,y=q.popleft()
            if (x,y) in v: continue
            v.add((x,y))
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1: q.append((nx,ny))
        return c-len(v)