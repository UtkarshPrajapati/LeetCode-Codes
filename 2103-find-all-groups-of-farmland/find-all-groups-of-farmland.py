class Solution:
    def findFarmland(self,land):
        res=[]
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j]==1 and i*land[i-1][j]==0 and j*land[i][j-1]==0:
                    row,col=i,j
                    while row<len(land) and land[row][j]==1: row+=1
                    while col<len(land[0]) and land[i][col]==1: col+=1
                    res.append([i,j,row-1,col-1])
        return res