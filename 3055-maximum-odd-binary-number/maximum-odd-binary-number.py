class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        c=s.count('1')
        if c==1: return "0"*(n-1)+"1"
        else: return (c-1)*"1"+(n-c)*"0"+"1"