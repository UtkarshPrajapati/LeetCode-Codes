class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]
        return sum(mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1 for i in range(m) for j in range(n))