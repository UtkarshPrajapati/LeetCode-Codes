class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i]==nums[j] for j in range(len(nums)) for i in range(j))