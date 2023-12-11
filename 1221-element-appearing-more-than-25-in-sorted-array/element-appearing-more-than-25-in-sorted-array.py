class Solution:
    def findSpecialInteger(self,arr):
        d=defaultdict(int)
        for i in arr:
            d[i]+=1
        return sorted(list(d.items()),key=lambda x:x[1],reverse=True)[0][0]