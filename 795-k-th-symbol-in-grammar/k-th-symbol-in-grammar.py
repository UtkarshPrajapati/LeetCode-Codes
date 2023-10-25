class Solution:
    def kthGrammar(self, n, k):
        k -= 1
        count = 0
        while k:
            k &= (k-1)
            count += 1
        return count & 1