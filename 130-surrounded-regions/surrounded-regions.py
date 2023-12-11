class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        q=deque([(i,j) for i in range(m) for j in range(n) if (i in [0,m-1] or j in [0,n-1]) and board[i][j]=='O'])
        while q:
            x,y=q.popleft()
            if 0<=x<m and 0<=y<n and board[x][y]=='O':
                board[x][y]='S'
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+dx,y+dy
                    q.append((nx,ny))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O': board[i][j]='X'
                elif board[i][j]=='S': board[i][j]='O'