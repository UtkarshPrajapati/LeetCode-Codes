class Solution:
    def maxProduct(self, arr):
        p,mp=1,float('-inf')
        for i in arr:
            p*=i
            mp=max(p, mp)
            if p==0: p=1
        p=1
        for i in reversed(arr):
            p*=i
            mp=max(p,mp)
            if p==0: p=1
        return mp