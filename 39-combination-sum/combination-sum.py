class Solution:
    def combinationSum(self,c,t):
        def dfs(t,index,path,res):
            if t<0: return
            if t==0: res.append(path);return 
            for i in range(index,len(c)): dfs(t-c[i],i,path+[c[i]],res)
        res=[]
        c.sort()
        dfs(t,0,[],res)
        return res