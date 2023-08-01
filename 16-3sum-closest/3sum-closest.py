class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        c=float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s<target: l+=1
                else: r-=1
                if abs(s-target)<abs(c-target): c=s
        return c
                