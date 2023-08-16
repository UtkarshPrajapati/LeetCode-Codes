class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat);t=sum(mat[i][i]+mat[i][n-1-i] for i in range(n))
        return [t,t-mat[n//2][n//2]][n&1]