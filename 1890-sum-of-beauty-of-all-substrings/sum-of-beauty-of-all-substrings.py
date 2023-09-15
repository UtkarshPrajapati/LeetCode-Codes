class Solution:
    def beautySum(self,s):
        cnt=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                c=Counter(s[i:j+1]).values()
                if c: cnt+=max(c)-min(c)
        return cnt