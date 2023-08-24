class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def f(cur):
            if cur in res: return
            res.append(cur)
            for i in range(len(cur)): f(cur[:i]+cur[i+1:])
        f(nums)
        return res