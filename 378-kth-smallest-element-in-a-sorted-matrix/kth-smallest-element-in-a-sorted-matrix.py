class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        l,r=matrix[0][0],matrix[n-1][n-1]
        while l<r:
            m=(l+r)//2
            c=0
            j=n-1
            for i in range(n):
                while j>=0 and matrix[i][j]>m: j-=1
                c+=j+1
            if c<k: l=m+1
            else: r=m
        return l