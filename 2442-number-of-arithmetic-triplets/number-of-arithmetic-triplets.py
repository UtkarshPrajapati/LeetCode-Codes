class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        a=set(nums) 
        return sum(i-diff in a and i+diff in a for i in nums)