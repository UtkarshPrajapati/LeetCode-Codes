class Solution:
    def minOperations(self,nums):
        n,nums,ans= len(nums),sorted(set(nums)),sys.maxsize
        return min(n-(bisect_right(nums,s+n-1)-i) for i,s in enumerate(nums))