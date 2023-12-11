class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n,fresh,rotten=len(grid),len(grid[0]),0,deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: fresh+=1
                elif grid[i][j]==2: rotten.append((i,j))
        cnt=0
        while rotten and fresh:
            cnt+=1
            for _ in range(len(rotten)):
                x,y=rotten.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        fresh-=1
                        grid[nx][ny]=2
                        rotten.append((nx,ny))
        return -1 if fresh!=0 else cnt