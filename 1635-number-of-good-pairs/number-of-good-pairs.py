class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i]==nums[j] for i,j in combinations(range(len(nums)),2) if i<j)