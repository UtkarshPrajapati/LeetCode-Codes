class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum(i<j<k and nums[j]-nums[i]==diff and nums[k]-nums[j]==diff for i in range(len(nums)) for j in range(len(nums)) for k in range(len(nums)))