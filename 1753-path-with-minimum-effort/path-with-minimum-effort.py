class Solution:
    def minimumEffortPath(self,h):
        rows,cols=len(h),len(h[0])
        d,minHeap=[(0,1),(0,-1),(1,0),(-1,0)],[(0,0,0)]
        dist=[[math.inf]*cols for _ in range(rows)]
        dist[0][0]=0
        while minHeap:
            effort,x,y=heappop(minHeap)
            if (x,y)==(rows-1,cols-1): return effort
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols:
                    new_effort=max(effort,abs(h[x][y]-h[nx][ny]))
                    if new_effort<dist[nx][ny]:
                        dist[nx][ny]=new_effort
                        heappush(minHeap,(new_effort,nx,ny))