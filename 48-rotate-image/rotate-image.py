class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix[0])
        for j in range(n):
            for i in range(j,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for j in range(len(matrix)):
            matrix[j].reverse()