class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        r1=[sum(i) for i in grid]
        r0=[m-i for i in r1]
        c1=[sum(j) for j in zip(*grid)]
        c0=[n-j for j in c1]
        return [[r1[i]-r0[i]+c1[j]-c0[j] for j in range(n)] for i in range(m)]