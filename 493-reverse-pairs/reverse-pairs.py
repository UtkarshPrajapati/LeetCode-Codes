class Solution:
    def reversePairs(self, nums):
        res=[0]
        def merge(nums):
            n=len(nums)
            if n<=1: return nums
            m=n//2
            left,right=merge(nums[:m]),merge(nums[m:])
            for r in right:
                res[0]+=len(left)-bisect.bisect(left,2*r)
                if not res[0]: break
            return sorted(left+right)
        merge(nums)
        return res[0]