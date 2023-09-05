class Solution:
    def generate(self, n: int) -> List[List[int]]:
        def nCr(n,r):
            res=1
            for i in range(r):
                res*=n-i
                res//=i+1
            return res
        return [[nCr(r,c) for c in range(r+1)] for r in range(n)]