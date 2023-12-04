class Solution:
    def numSubarraysWithSum(self,nums,goal):
        s,c,d=0,0,defaultdict(int)
        d[0]=1
        for i in nums:
            s+=i
            if s-goal in d: c+=d[s-goal]
            d[s]+=1
        return c