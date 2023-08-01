class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        c = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                l, r = (l + 1, r) if s < target else (l, r - 1)
                c = s if abs(s - target) < abs(c - target) else c
        return c