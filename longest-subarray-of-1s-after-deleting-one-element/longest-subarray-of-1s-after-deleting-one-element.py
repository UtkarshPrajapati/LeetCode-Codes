class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n,left,zeros,ans = len(nums),0,0,0
        for right in range(n):
            if nums[right] == 0: zeros += 1
            while zeros>1:
                if nums[left] == 0: zeros -= 1
                left += 1
            ans = max(ans, right - left + 1 - zeros)
        return ans-1 if ans==n else ans