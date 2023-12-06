class Solution:
    def insert(self,intv,ni):
        res=[]
        for i in range(len(intv)):
            if intv[i][1]<ni[0]: res.append(intv[i])
            elif intv[i][0]>ni[1]: return res+[ni]+intv[i:]
            else: ni=[min(ni[0],intv[i][0]),max(ni[1],intv[i][1])]
        return res+[ni]