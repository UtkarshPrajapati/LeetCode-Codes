class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums);lc=[[1,1] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    t=lc[j][0]+1
                    if t>lc[i][0]: lc[i]=[t,lc[j][1]]
                    elif t==lc[i][0]: lc[i][1]+=lc[j][1]
        m=max([x[0] for x in lc])
        return sum(x[1] for x in lc if x[0]==m)