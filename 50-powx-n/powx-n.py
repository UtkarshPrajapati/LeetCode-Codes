class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        if n<0: return 1/self.myPow(x,-n)
        t=self.myPow(x, n // 2);y=t*t
        return x*y if n&1 else y