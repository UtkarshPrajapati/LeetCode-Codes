class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(c):
            if len(c)==len(nums): a.append(c[:]);return
            for i in nums:
                if i not in c: bt(c+[i])
        a=[]
        bt([])
        return a