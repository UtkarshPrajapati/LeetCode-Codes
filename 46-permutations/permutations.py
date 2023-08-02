class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(c):
            if len(c)==len(nums): a.append(c[:]);return
            for i in nums:
                if i not in c:
                    c.append(i)
                    bt(c)
                    c.pop()
        a=[]
        bt([])
        return a