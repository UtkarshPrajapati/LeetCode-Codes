class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=list(map(int,str(n)))
        m=1
        for i in a:
            m*=i
        return m-sum(a)