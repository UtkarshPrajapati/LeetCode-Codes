class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums);l=[1]*n;c=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    t=l[j]+1
                    if t>l[i]: l[i],c[i]=t,c[j]
                    elif t==l[i]: c[i]+=c[j]
        m=max(l)
        return sum(c[i] for i in range(n) if l[i] ==m)