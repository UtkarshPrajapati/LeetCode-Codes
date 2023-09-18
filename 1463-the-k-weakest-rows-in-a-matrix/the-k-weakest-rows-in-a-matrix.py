class Solution:
    def kWeakestRows(self,mat,k):
        return [sorted([[i,sum(mat[i])] for i in range(len(mat))],key=lambda x:x[1])[i][0] for i in range(k)]