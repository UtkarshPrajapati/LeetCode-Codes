class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=list(map(int,str(n)))
        return reduce(mul,a)-sum(a)