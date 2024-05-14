class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        def f(i,j,vis):
            t=[]
            if i+1<m and grid[i+1][j]!=0 and (i+1,j) not in vis: t.append(f(i+1,j,vis|{(i,j)}))
            if i-1>=0 and grid[i-1][j]!=0 and (i-1,j) not in vis: t.append(f(i-1,j,vis|{(i,j)}))
            if j+1<n and grid[i][j+1]!=0 and (i,j+1) not in vis: t.append(f(i,j+1,vis|{(i,j)}))
            if j-1>=0 and grid[i][j-1]!=0 and (i,j-1) not in vis: t.append(f(i,j-1,vis|{(i,j)}))
            return grid[i][j]+max(t,default=0)

        l=[]
        vis=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0: l.append(f(i,j,vis))
        return max(l,default=0)
        