class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=list(Counter(nums).values())
        m=max(c)
        return c.count(m)*m