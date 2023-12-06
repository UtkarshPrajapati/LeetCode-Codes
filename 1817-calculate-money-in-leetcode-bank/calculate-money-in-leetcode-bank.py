class Solution:
    def totalMoney(self, n: int) -> int:
        s=0

        for i in range(n//7):
            s+=(7+i)*(8+i)//2-(i*(i+1))//2
        for i in range(n%7):
            s+=(n//7+1)+i
        return s