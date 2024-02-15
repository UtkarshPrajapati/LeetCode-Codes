class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ps=[nums[0]]
        maxx=-1
        for i in range(1,len(nums)):
            ps.append(ps[-1]+nums[i])
        for i in range(1,len(ps)-1):
            if ps[i]>nums[i+1]: maxx=ps[i+1]
        return maxx