class Solution:
    def solveNQueens(self, n):
        def solve(queens=[], xy_dif=[], xy_sum=[]):
            p = len(queens)
            if p==n: result.append(queens)
            else:
                for q in range(n):
                    if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                        solve(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        solve()
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]