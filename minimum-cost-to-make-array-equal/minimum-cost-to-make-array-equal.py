class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def fcost(l):
            tc = 0
            for i, x in enumerate(nums): tc += abs(l - x) * cost[i]
            return tc
        l,r = min(nums),max(nums) + 1
        m = (l + r) // 2
        while l < r:
            if fcost(m) < fcost(m + 1): r = m
            else: l = m + 1
            m = (l + r) // 2
        return fcost(l)