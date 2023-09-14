class Solution:
    def removeOuterParentheses(self,S):
        ans,n=[],0
        for c in S:
            if c=='(' and n>0 or c==')' and n>1: ans.append(c)
            n+=1 if c=='(' else -1
        return "".join(ans)