class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[(m:=(l+r)//2)] == t: return m
            if nums[l] <= nums[m]: l,r=(l,m-1) if nums[l] <= t < nums[m] else (m+1,r)
            else: l,r=(m+1,r) if nums[m] < t <= nums[r] else (l,m-1)
        return -1