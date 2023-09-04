class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c,cs,ps=0,0,{0:1}
        for i in nums:
            cs+=i
            if cs-k in ps: c+=ps[cs-k]
            ps[cs]=ps.get(cs,0)+1
        return c