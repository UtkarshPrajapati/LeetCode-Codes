class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, mp, l = 0, {}, 0
        for r, num in enumerate(nums):
            mp[num] = mp.get(num, 0) + 1
            while mp[num] > k:
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans