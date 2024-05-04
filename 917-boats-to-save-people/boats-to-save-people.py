class Solution:
    def numRescueBoats(self,p,limit):
        p.sort()
        ans,i,j=0,0,len(p)-1
        while i<=j:
            if p[i]+p[j]<=limit: i+=1
            j-=1
            ans+=1
        return ans