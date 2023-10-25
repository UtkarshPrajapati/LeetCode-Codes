class Solution:
    def kthGrammar(self,n,k):
        return bin(k-1).count('1')&1