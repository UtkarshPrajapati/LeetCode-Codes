class Solution:
    def smallestSufficientTeam(self,req_sk,p):
        m,n=len(req_sk),len(p)
        c=[sum(1<<{v:i for i,v in enumerate(req_sk)}[skill] for skill in skills) for skills in p]
        @cache
        def fn(i,mask):
            if mask==0: return []
            if i==n: return [0]*100
            if not (mask&c[i]): return fn(i+1,mask)
            return min(fn(i+1,mask),[i]+fn(i+1,mask&~c[i]),key=len)
        return fn(0,(1<<m)-1)