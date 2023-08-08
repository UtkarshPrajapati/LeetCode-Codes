class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,n=nums.index(max(nums)),len(nums)
        nums=nums[a+1:]+nums[:a+1]
        l,r=0,n-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target: return (m+a+1)%n
            l,r=(l,m-1) if target<nums[m] else (m+1,r)
        return -1