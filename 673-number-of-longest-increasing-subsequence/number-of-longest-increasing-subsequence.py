class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def upd(t,i,v):
            while i<=len(t)-1:
                if v[0]>t[i][0]: t[i]=v[:]
                elif v[0]==t[i][0]: t[i][1]+=v[1]
                i+=i&-i
        def qry(t,i):
            r=[0,0]
            while i>0:
                if t[i][0]>r[0]: r=t[i][:]
                elif t[i][0]==r[0]: r[1]+=t[i][1]
                i-=i&-i
            return r
        n,sn=len(nums),sorted(set(nums));ind={num:i+1 for i,num in enumerate(sn)}
        bit=[[0,0] for _ in range(len(sn)+1)]
        for num in nums:
            i=ind[num];l,c=qry(bit,i-1)
            upd(bit,i,[l+1,max(c,1)])
        return qry(bit,len(sn))[1]