class Solution:
    def kthGrammar(self,n,k):
        k,c=k-1,0
        while k:
            k,c=k&(k-1),c+1
        return c&1