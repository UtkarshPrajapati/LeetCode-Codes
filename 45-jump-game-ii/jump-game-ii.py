class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2: return 0
        mp=ms=nums[0]
        jumps=1
        for i in range(1,n):
            if ms<i: jumps+=1;ms=mp
            mp=max(mp,nums[i]+i)
        return jumps