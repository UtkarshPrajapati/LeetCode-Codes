class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        p=[]
        for i in range(n//2):
            p.append((nums[i],nums[n-i-1]))
        return max(a+b for a,b in p)