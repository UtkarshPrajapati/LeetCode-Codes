class Solution:
    def customSortString(self,order,s):
        c,ans=Counter(s),""
        return "".join([i*c[i] for i in order if i in c])+"".join([i*c[i] for i in set(s)-set(order)])