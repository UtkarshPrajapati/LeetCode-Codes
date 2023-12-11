class Solution:
    def updateMatrix(self,mat):
        if not mat or not mat[0]: return []
        m,n,q=len(mat),len(mat[0]),deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0: q.append((i,j))
                else: mat[i][j]=m*n
        while q:
            x,y=q.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and mat[nx][ny]>mat[x][y]+1:
                    q.append((nx,ny))
                    mat[nx][ny]=mat[x][y]+1
        return mat