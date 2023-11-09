class Solution:
    def countHomogenous(self,s):
        return sum((n:=len(list(g)))*(n+1)//2 for k,g in groupby(s))%1000000007