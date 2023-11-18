class Solution:
    def maxFrequency(self,nums,k):
        nums.sort()
        heap,t,ans=[],0,0
        for n in nums:
            heappush(heap,n)
            t+=n
            while t+k<n*len(heap):
                t-=heappop(heap)
            ans=max(ans,len(heap))
        return ans