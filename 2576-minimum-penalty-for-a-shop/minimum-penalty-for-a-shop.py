class Solution:
    def bestClosingTime(self,cus):
        ans=o=cus.count('Y')
        res=0
        for i,c in enumerate(cus):
            if c=='Y': o-=1
            else: o+=1
            if o<ans: ans,res=o,i+1
        return res