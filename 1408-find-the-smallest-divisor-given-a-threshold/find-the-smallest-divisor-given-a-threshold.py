class Solution:
    def smallestDivisor(self, nums: List[int], t: int) -> int:
        l,r=1,max(nums)
        while l<r:
            m=(l+r)//2
            s=sum((i+m-1)//m for i in nums)
            if s>t: l=m+1
            else: r=m
        return l