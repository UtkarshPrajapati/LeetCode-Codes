class Solution:
    def titleToNumber(self, s: str) -> int:
        c,k=0,1
        for i in list(s)[::-1]:
            c+=(ord(i)-64)*k
            k*=26
        return c