class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        c,r=set(),set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0: r.add(i);c.add(j)
        for i in range(m):
            if i in r: matrix[i]=[0]*n
        for j in range(n):    
            if j in c: 
                for i in range(m):
                    matrix[i][j]=0