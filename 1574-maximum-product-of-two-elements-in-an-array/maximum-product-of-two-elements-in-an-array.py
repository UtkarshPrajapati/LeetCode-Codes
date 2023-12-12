class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nlargest(2,nums)
        return (a[0]-1)*(a[1]-1)