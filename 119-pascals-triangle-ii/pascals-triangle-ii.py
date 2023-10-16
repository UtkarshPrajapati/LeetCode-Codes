class Solution:
    def getRow(self,n):
        row=[1]
        for _ in range(n):
            row=[x+y for x,y in zip([0]+row,row+[0])]
        return row