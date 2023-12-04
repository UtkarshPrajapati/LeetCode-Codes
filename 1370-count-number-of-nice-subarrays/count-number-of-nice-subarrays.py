class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s,c,d=0,0,defaultdict(int)
        d[0]=1
        for i in nums:
            s+=i%2
            if s-k in d: c+=d[s-k]
            d[s]+=1
        return c