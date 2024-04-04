class Solution:
    def maxDepth(self,s):
        c,ans=0,0
        for i in s:
            if i=='(':
                c+=1
                if c>ans: ans=c
            elif i==')': c-=1
        return ans