class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n,q,v=len(image),len(image[0]),deque([(sr,sc)]),set([(sr,sc)])
        pc=image[sr][sc]
        while q:
            x,y=q.popleft()
            image[x][y]=color
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and image[nx][ny]==pc and (nx,ny) not in v:
                    image[nx][ny]=color
                    q.append((nx,ny))
                    v.add((nx,ny))
        return image