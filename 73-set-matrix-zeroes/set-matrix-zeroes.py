class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        rm,c,r=range(m),set(),set()
        for i in rm:
            for j in range(n):
                if matrix[i][j]==0: r.add(i);c.add(j)
        for i in rm:
            if i in r: matrix[i]=[0]*n
        for j in c:    
            for i in rm: matrix[i][j]=0