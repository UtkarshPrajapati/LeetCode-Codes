class Solution:
    def customSortString(self,order,s):
        c=Counter(s)
        return "".join(i*c[i] for i in order if i in c)+"".join(i*c[i] for i in c.keys()-order)