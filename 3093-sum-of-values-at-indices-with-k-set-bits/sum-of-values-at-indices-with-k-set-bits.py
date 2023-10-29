class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(n for i,n in enumerate(nums) if k==i.bit_count())