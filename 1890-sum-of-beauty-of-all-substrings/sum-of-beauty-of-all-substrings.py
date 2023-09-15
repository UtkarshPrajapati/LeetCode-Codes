class Solution:
    def beautySum(self,s):
        cnt=0
        for i in range(len(s)):
            c=Counter()
            for j in range(i,len(s)):
                c[s[j]]+=1
                if c: cnt+=max(c.values())-min(c.values())
        return cnt