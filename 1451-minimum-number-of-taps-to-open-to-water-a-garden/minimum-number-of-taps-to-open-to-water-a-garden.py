class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        m=[0]*(n+1)
        for i,r in enumerate(ranges):
            l,r=max(0,i-r),min(n,i+r)
            m[l]=max(m[l],r)
        start=end=c=0
        while end<n:
            c+=1
            start,end=end,max(m[start:end+1])
            if start==end: return -1
        return c