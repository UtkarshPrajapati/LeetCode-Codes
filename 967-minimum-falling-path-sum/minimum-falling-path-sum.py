class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:  
        l=len(m)
        for i in range(1,l):
            for j in range(l):
                m[i][j]+=min(m[i-1][max(0,j-1):min(l,j+2)])
        return min(m[-1])