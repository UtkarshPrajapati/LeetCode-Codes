class Solution:
    def combine(self,n,k):
        res,stk=[],[(i,[i]) for i in range(n,0,-1)]
        while stk:
            node,path=stk.pop()
            res+=[path]*(len(path)==k)
            stk+=[(i,path+[i]) for i in range(node-1,0,-1)]
        return res