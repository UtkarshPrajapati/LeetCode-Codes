class Solution:
    def kthGrammar(self,n,k):
        return (k-1).bit_count()%2