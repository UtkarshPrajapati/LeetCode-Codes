class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        return [i for i,c in Counter(nums).items() if c>n//3]