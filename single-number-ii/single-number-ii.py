class Solution:
    def singleNumber(self, nums):
        d=defaultdict(int)
        for x in nums:
            d[x]+=1
        for x,f in d.items():
            if f==1: return x
        return -1